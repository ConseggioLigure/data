#!/usr/bin/env python3

import argparse
import re
import subprocess
import tempfile
from pathlib import Path

parser = argparse.ArgumentParser(description="Export Ligurian patterns for libhyphen.")
parser.add_argument("source", type=Path, help="upstream hyph-lij.tex")
parser.add_argument("substrings", type=Path, help="libhyphen 2.8.9 substrings.pl")
parser.add_argument("output", type=Path)
args = parser.parse_args()

source = args.source.read_text(encoding="utf-8")
match = re.fullmatch(r"((?:%[^\n]*\n)*)\\patterns\{\s*(.*?)\s*\}\s*", source, re.S)
if not match:
    parser.error("expected a comment header followed by one TeX patterns block")
comments, patterns = match.groups()
patterns = re.sub(r"%[^\n]*", "", patterns).strip()
if not re.fullmatch(r"[.0-9a-z'à-ü’\s]+", patterns):
    parser.error("unexpected Ligurian pattern syntax")

with tempfile.TemporaryDirectory() as temporary:
    raw = Path(temporary) / "patterns.txt"
    converted = Path(temporary) / "hyph.dic"
    # substrings.pl 2.8.9 skips the first non-comment line.
    raw.write_text("\n" + patterns + "\n", encoding="utf-8")
    subprocess.run(
        ["perl", args.substrings, raw, converted],
        check=True,
        stdout=subprocess.DEVNULL,
    )
    exported = converted.read_text(encoding="utf-8")

if not exported.strip():
    parser.error("substrings.pl produced no patterns")
args.output.write_text(
    f"UTF-8\nLEFTHYPHENMIN 2\nRIGHTHYPHENMIN 2\n{comments}NEXTLEVEL\n{exported}",
    encoding="utf-8",
)
