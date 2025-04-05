#!/bin/bash


python app.py &


sleep 5


mkdir -p tests/results


pytest -s -v tests/test_app_api.py > tests/results/api_results.txt
