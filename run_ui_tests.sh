#!/bin/bash


python app.py &


sleep 5


mkdir -p tests/results


pytest -s -v tests/test_list_cars_ui.py > tests/results/ui_results.txt
