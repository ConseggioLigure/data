# Ligurian language resources

This repository hosts language technology resources for Ligurian made available by the [Council for Ligurian Linguistic Heritage](https://conseggio-ligure.org/en/) (*Conseggio pe-o patrimònio linguistico ligure*). It also lists other resources for machine translation, speech recognition and related technologies.

## Linguistic scope and data curation

Genoese is the shared regional variety of Ligurian and its principal literary form. Its codified modern orthography is documented in [DEIZE](https://conseggio-ligure.org/en/dictionary/deize).

Ligurian also includes a number of local varieties, while Genoese itself may be written according to different spelling conventions. For corpus construction and language modelling, these distinctions should be taken into account when selecting and combining sources.

Publicly available text collections, including sources such as Wikipedia, can be valuable for language technology, but may contain a mixture of varieties, spelling systems and levels of editorial consistency. They are therefore best used with appropriate source review and, where relevant, linguistic labelling rather than treated as authoritative reference data.

## Resources

Each resource has its own licence, specified below. Consult the corresponding licence file or dataset documentation for its terms of use.

### Hunspell dictionary

The [Hunspell dictionary](hunspell-lij/) provides spell checking for Ligurian (Genoese). Its lexical content and spelling conventions derive from [DEIZE](https://conseggio-ligure.org/en/dictionary/deize) (*Diçionäio elettrònico italian-zeneise*), the Council’s bilingual Italian-Ligurian dictionary, edited by Jean Maillard with linguistic support from Stefano Lusito.

Released under the [MIT License](hunspell-lij/LICENSE).

### Hyphenation patterns

The [TeX hyphenation patterns](hyph-lij/) for Genoese were developed for [*Zimme de braxa*](https://conseggio-ligure.org/en/zimme-de-braxa/), the Council’s Ligurian literature series, in collaboration with [Editrice Zona](https://editricezona.it/).

Released under the [MIT License](hyph-lij/LICENSE).

### Machine translation

* [ZenaMT](https://huggingface.co/datasets/ConseggioLigure/zenamt) is an Italian-Ligurian (Genoese) parallel corpus covering domains of cultural relevance to Ligurian speakers, with English translations for some texts. Released under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

* [OLDI Seed](https://huggingface.co/datasets/openlanguagedata/oldi_seed) is a multilingual parallel corpus for machine translation, including Ligurian. It is an updated and improved version of NLLB-Seed. Released under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

* [FLORES+](https://huggingface.co/datasets/openlanguagedata/flores_plus) is a multilingual machine translation benchmark that includes Ligurian. It is an updated and improved version of FLORES-200. Released under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

* [SMOL](https://huggingface.co/datasets/google/smol) provides sentence- and document-level translations for machine translation, including Ligurian. Released under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

* [GATITOS](https://huggingface.co/datasets/google/smol) is a multilingual parallel lexicon of words and short phrases, including Ligurian, distributed with SMOL. Released under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

* [BOUQuET](https://huggingface.co/datasets/facebook/bouquet) is a multilingual translation benchmark covering multiple domains and registers, including Ligurian. Released under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

### Speech

* [Omnilingual ASR Corpus](https://huggingface.co/datasets/facebook/omnilingual-asr-corpus) provides speech recordings and transcriptions for automatic speech recognition, including Ligurian. Released under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

### Text normalization

* [Normalized Ligurian corpus](normalization/) is a collection of sentences written in historical spellings, paired with their normalized versions. It can be used to train text-normalization systems. Released under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

### Dependency parsing

* [UD Ligurian GLT](https://github.com/UniversalDependencies/UD_Ligurian-GLT/) is a [Universal Dependencies](https://universaldependencies.org/) treebank for Ligurian. Released under [C-UDA 1.0](https://spdx.org/licenses/C-UDA-1.0.html).
