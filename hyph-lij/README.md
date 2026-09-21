# Hyphenation patterns for Ligurian (Genoese)

Current release: **26.0921**.

These hyphenation patterns were developed by the [Council for Ligurian Linguistic Heritage](https://conseggio-ligure.org/en/) for the typesetting of [*Zimme de braxa*](https://conseggio-ligure.org/en/zimme-de-braxa/), its Ligurian literature book series. The series is published in collaboration with [Editrice Zona](https://editricezona.it/).

The patterns follow the codified modern spelling of Genoese, the shared regional variety of Ligurian and its principal literary form.

They have been written assuming the applications that use them have a setting equivalent to `hyphenmins={2,2}` or greater. When exporting for libhyphen/LibreOffice, `NEXTLEVEL` needs to be inserted before all patterns, to disables libhyphen’s default apostrophe compound splitting. To convert these patterns for libhyphen, we provide the script `export_libhyphen.py` for convenience.

## Development

Run `uv run tests/test_hyphenation.py` from the repository root. The tests use [Pyphen](https://pyphen.org/) 0.18.1; expected hyphenations are listed in [`tests/hyph-lij.hyph`](../tests/hyph-lij.hyph).

## License

Copyright © 2023-2026 Edoardo Ferrante, Stefano Lusito and Jean Maillard

The hyphenation patterns in `hyph-lij.tex` are released under the [MIT License](LICENSE).

## Contact

For corrections or integration questions please contact [info@conseggio-ligure.org](mailto:info@conseggio-ligure.org).
