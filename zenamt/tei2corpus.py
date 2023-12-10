import argparse
import re
import xml.etree.ElementTree as ET
from contextlib import ExitStack
from pathlib import Path


def find_element(ancestor, element_id):
    for element in ancestor.iter():
        if element.get(f"{{{NS['xml']}}}id") == element_id:
            return element
    raise ValueError(f"Id not found: {element_id} in {ancestor}")


def get_alignment_text(ancestor, element_id, debug=False):
    def get_textual_content(element):
        text = element.text or ""
        for child in element:
            text += get_textual_content(child)
            if child.tail:
                text += child.tail
        text = re.sub(r"\s+", " ", text)
        return text.strip()

    element = find_element(ancestor, element_id)

    if element.tag.endswith("ptr"):
        targets = element.get("target").split()
        lang = find_element(ancestor, targets[0][1:]).get(f"{{{NS['xml']}}}lang")
        elements = [find_element(ancestor, t[1:]) for t in targets]
        text = " ".join(
            get_textual_content(el) for el in elements
        )
    else:
        lang = element.get(f"{{{NS['xml']}}}lang")
        text = get_textual_content(element)
    if debug:
        text = f"[{element_id}] {text}"
    return lang, text


parser = argparse.ArgumentParser()
parser.add_argument("src_file", type=Path)
parser.add_argument("out_prefix", type=Path)
parser.add_argument("--langs", "-l", type=str, nargs="+", default="lij ita".split())
parser.add_argument(
    "--format",
    "-f",
    choices="sentence document".split(),
    default="sentence",
    help="Extract sentence- or document-level aligned corpus",
)
parser.add_argument(
    "--exclude-ids",
    nargs="+",
    default=[],
    help="Exclude all elements that have one of these strings in their xml:id",
)
parser.add_argument(
    "--only-ids",
    nargs="+",
    help="Only include elements that have one of these strings in their xml:id",
)
parser.add_argument(
    "--debug",
    action="store_true",
)
args = parser.parse_args()

if args.format == "document":
    raise NotImplementedError

args.out_prefix.parent.mkdir(parents=True, exist_ok=True)

NS = {
    "tei": "http://www.tei-c.org/ns/1.0",
    "xml": "http://www.w3.org/XML/1998/namespace",
}

tree = ET.parse(args.src_file)
corpus = tree.getroot()

assert corpus.tag in (f"{{{NS['tei']}}}teiCorpus", f"{{{NS['tei']}}}TEI"), corpus.tag

with ExitStack() as stack:
    fs = [
        stack.enter_context(open(args.out_prefix.parent / f"{args.out_prefix.name}.{l}", "wt"))
        for l in args.langs
    ]

    for link in corpus.findall(
        f".//tei:linkGrp[@type='translation']/tei:link[@target]", namespaces=NS
    ):
        ids = link.get("target").split()

        # Ensure the ids are not in the exclusion list args.exclude_ids
        if args.exclude_ids:
            if any(ei in i for ei in args.exclude_ids for i in ids):
                continue

        # Ensure the ids are in args.only_ids, if specified
        if args.only_ids:
            if all(oi not in i for oi in args.only_ids for i in ids):
                continue

        texts = dict(get_alignment_text(corpus, i[1:], args.debug) for i in ids)

        for i, lang in enumerate(args.langs):
            try:
                print(texts[lang], file=fs[i])
            except KeyError:
                print(f"Missing lang {lang} in:")
                print(texts)
                raise
