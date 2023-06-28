#!/bin/bash
EXIT_CODE=0
echo "Running test"
poetry run pytest --json-report || EXIT_CODE=$?

echo "Printing out report"
OUTCOME=$(cat .report.json | jq -r '.tests[]|"\(.outcome),\(.nodeid)"')

declare -A SCORE
SCORE["test_q1_test_find_richest_and_asset"]=10
SCORE["test_q1_test_find_top3_richest_city"]=20
SCORE["test_q2_test_find_corp_total_asset"]=10
SCORE["test_q2_test_find_llc_total_asset"]=10
SCORE["test_q3_test_summarize"]=20
SCORE["test_q4_test_find_poor_and_asset"]=10
SCORE["test_q4_test_find_top3_poorest_city"]=20

TOTAL=0
while IFS= read -r line; do
  echo "Processing line: $line"

  IFS=',' read -r outcome nodeid <<< "$line"

  TEST_ID=$(echo $nodeid | awk -F"::" '{print $2}')
  if [ "$outcome" = "passed" ]; then
    echo "Test $TEST_ID passed, Adding ${SCORE[$TEST_ID]}"
    TOTAL=$((TOTAL+${SCORE[$TEST_ID]}))
  else
    echo "Test $TEST_ID $outcome"
  fi
done <<< "$OUTCOME"
echo "Total score: $TOTAL"
exit $EXIT_CODE
