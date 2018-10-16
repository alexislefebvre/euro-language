#!/usr/bin/env bash

OUTPUT="test/output.txt"
EXPECTED_OUTPUT="test/expected_output.txt"

# launch test and store output
python euro.py euro.eu > "${OUTPUT}"

# compare that output is the same as expected output
# see https://serverfault.com/questions/674358/how-to-test-if-two-given-files-are-identical/674379#674379
if cmp --silent "${EXPECTED_OUTPUT}" "${OUTPUT}" ; then
   echo "Files are identical"
   exit 0
else
   echo "Files are different, diff:"
   diff -u "${EXPECTED_OUTPUT}" "${OUTPUT}"
   exit 1
fi
