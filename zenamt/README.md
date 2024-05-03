# ZenaMT corpus

This is an Italian – Genoese Ligurian parallel corpus covering a number of domains of cultural relevance to Ligurian speakers. Parts of the corpus also contain aligned English translations. The data is being extracted from a variety of sources.

| Corpus        | Domain | Languages | Train | Valid | Test |
|---------------|--------|-----------|-------|-------|------|
| `linguistics` | Example sentences from an [Italian-Genoese dictionary](https://conseggio-ligure.org/en/dictionary/deize/) and other Ligurian study materials. | Ligurian, Italian | 3,497 |
| `news`        | News from the weekly Ligurian news website [O Zinâ](https://www.ozina.org) | Ligurian, Italian | 2,471 | 130 | 264 |
| `literature`  | Essays on the history of Ligurian literature. | Ligurian, Italian, English | 724 | 135 | 207 |
| `entities`    | Purpose-built parallel sentence lists covering Ligurian toponyms and other culturally-relevant named entities. | Ligurian, Italian | 414 | 103 | 104 |
| `dialogues`  | Scripted dialogues. | Ligurian, Italian | 441 | 30 | 48 |
| `games`       | Rule description of traditional Ligurian card games. | Ligurian, Italian, English | 297 | | |

The subcorpora can be downloaded from their respective subfolders. They are available in sentence-aligned format as pairs of plain text files (with extensions corresponding to the language). Some subcorpora are also available in document-aligned format – please refer to the `.xml` TEI files, where available.

> [!NOTE]
> This is a living corpus. It will receive updates as the sources it draws from keep growing.

<p xmlns:cc="http://creativecommons.org/ns#" >This work is licensed under <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY 4.0<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"></a></p>

## Attribution

If you use this corpus in your own work, please cite the following paper:
```bibtex
@article{zenamt24,
  title={Italian-Ligurian Machine Translation in its Cultural Context},
  author={Haberland, Christopher and Lusito, Stefano and Maillard, Jean},
  booktitle={Proceedings of the 3rd Annual Meeting of the ELRA/ISCA Special Interest Group on Under-Resourced Languages},
  year={2024},
}
```
