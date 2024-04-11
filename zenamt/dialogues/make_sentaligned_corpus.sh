#!/bin/sh

TEST_IDS="besagnin biggetto-treno"
VALID_IDS="travaggi che-autobo"

python ../tei2corpus.py dialogues.xml test_dialogues \
  -l lij ita \
  --only-ids ${TEST_IDS}

python ../tei2corpus.py dialogues.xml valid_dialogues \
  -l lij ita \
  --only-ids ${VALID_IDS}

python ../tei2corpus.py dialogues.xml train_dialogues \
  -l lij ita \
  --exclude-ids ${TEST_IDS} ${VALID_IDS}
