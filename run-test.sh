#!/bin/bash
EXIT_CODE=0
echo "Running test"
poetry run pytest --json-report || EXIT_CODE=$?

echo "Printing out report"
cat .report.json

echo "Exit"
exit $EXIT_CODE
