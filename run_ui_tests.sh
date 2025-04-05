#!/bin/bash


python app.py &


sleep 5


mkdir -p tests/results


pytest -s -v tests/test_list_cars.py > tests/results/ui_results.txt
