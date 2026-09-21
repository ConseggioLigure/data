# /// script
# requires-python = ">=3.10"
# dependencies = ["pyphen==0.18.1"]
# ///

import re
import sys
from pathlib import Path
from tempfile import TemporaryDirectory

import pyphen

directory = Path(__file__).resolve().parent
source = (directory.parent / "hyph-lij" / "hyph-lij.tex").read_text(encoding="utf-8")
left = int(re.search(r"left:\s*(\d+)", source)[1])
right = int(re.search(r"right:\s*(\d+)", source)[1])
if min(left, right) < 2:
    sys.exit("Hyphenation minima must both be at least 2")
patterns = re.search(r"\\patterns\s*{([^}]*)}", re.sub(r"%[^\n]*", "", source))[1]
with TemporaryDirectory() as temporary:
    dictionary = Path(temporary) / "hyph_lij.dic"
    dictionary.write_text("UTF-8\n" + "\n".join(patterns.split()), encoding="utf-8")
    hyphenator = pyphen.Pyphen(filename=dictionary, left=left, right=right)

cases = (directory / "hyph-lij.hyph").read_text(encoding="utf-8").split()
if not cases:
    sys.exit("No test cases found")
failed = 0
for number, expected in enumerate(cases, 1):
    actual = hyphenator.inserted(expected.replace("-", ""))
    if actual != expected:
        print(f"FAIL test {number}: expected {expected}; got {actual}")
        failed += 1
print(f"{len(cases) - failed}/{len(cases)} tests passed")
sys.exit(bool(failed))
