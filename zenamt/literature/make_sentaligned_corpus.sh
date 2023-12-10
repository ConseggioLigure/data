#!/bin/sh

TEST_IDS="anonimo-zeneise uxi-officiae-da-lengua-zeneise brunna-pedemonte francesco-maria-marin sandro-patron togno-lea sergio-sileri roberto-giannon andreinna-soa scirvio-opisso gioxeppe-cascinelli cesare-vivado freirigo-gazzo gioxeppe-cava nicolo-bacigalo martin-piaggio giornali-do-sec-xix vito-elio-petrucci rita-cuneo primmi-scrittoi-da-rivea roberto-benso"
VALID_IDS="reixe-da-lengua-ligure descorsci-do-sec-xv lusciandro-guason zane-andria-spinoa vicenso-jacono italo-mario-angeloni plinio-guidon pia-viale andria-capan franco-d-imporsan marco-carbon danila-oive"

python ../tei2corpus.py literature.xml test \
  -l lij ita eng \
  --only-ids ${TEST_IDS}

python ../tei2corpus.py literature.xml valid \
  -l lij ita eng \
  --only-ids ${VALID_IDS}

python ../tei2corpus.py literature.xml train \
  -l lij ita eng \
  --exclude-ids ${TEST_IDS} ${VALID_IDS}