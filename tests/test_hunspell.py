import subprocess
import sys
from pathlib import Path
from unicodedata import normalize

directory = Path(__file__).resolve().parent
accepted, rejected = (
    sorted(
        {
            normalize(form, word)
            for word in (directory / f"lij_IT.{expectation}")
            .read_text(encoding="utf-8")
            .split()
            for form in ("NFC", "NFD")
        }
    )
    for expectation in ("accept", "reject")
)
result = subprocess.run(
    [
        "hunspell",
        "-l",
        "-i",
        "UTF-8",
        "-p",
        "/dev/null",
        "-d",
        str(directory.parent / "hunspell-lij" / "lij_IT"),
    ],
    input="\n".join(accepted + rejected) + "\n",
    stdout=subprocess.PIPE,
    encoding="utf-8",
    check=True,
).stdout.split()
errors = [f"Wrongly rejected: {word}" for word in sorted(set(result) - set(rejected))]
errors += [f"Wrongly accepted: {word}" for word in sorted(set(rejected) - set(result))]
if errors:
    sys.exit("\n".join(errors))
print(f"{len(accepted) + len(rejected)} tests passed")
