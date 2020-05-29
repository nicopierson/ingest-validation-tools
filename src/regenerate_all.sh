#!/usr/bin/env bash
set -o errexit

(echo '```'; src/generate_docs.py -h; echo '```') > README-generate_docs.py.md
(echo '```'; src/validate_submission.py -h; echo '```') > README-validate_submission.py.md
for D in `ls -d docs/*/`; do src/generate_docs.py `basename $D` $D; done