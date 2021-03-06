#!/usr/bin/env bash
set -o errexit

red=`tput setaf 1`
reset=`tput sgr0`
die() { set +v; echo "$red$*$reset" 1>&2 ; exit 1; }

for EXAMPLE in dataset-examples/*; do
  echo "Testing $EXAMPLE ..."
  CMD="src/validate_submission.py \
--local_directory $EXAMPLE/submission \
--dataset_ignore_globs 'ignore-*.tsv' '.*' \
--submission_ignore_globs 'drv_ignore_*' \
--output as_md"
  README="$EXAMPLE/README.md"
  diff $README <( eval "$CMD" ) \
    || die "Update example: $CMD > $README"
done

for GOOD in dataset-examples/good-*/README.md; do
  grep 'No errors!' $GOOD > /dev/null || die "$GOOD should not be an error report."
done

for BAD in dataset-examples/bad-*/README.md; do
  ! grep 'No errors!' $BAD || die "$BAD should be an error report."
done
