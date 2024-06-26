#!/bin/sh

TEST_IDS="z230630 z230707 z240105 z240112"
VALID_IDS="z230728 z240202"

python ../tei2corpus.py news.xml test_news \
  -l lij ita \
  --only-ids ${TEST_IDS}

python ../tei2corpus.py news.xml valid_news \
  -l lij ita \
  --only-ids ${VALID_IDS}

python ../tei2corpus.py news.xml train_news \
  -l lij ita \
  --exclude-ids ${TEST_IDS} ${VALID_IDS}
  
