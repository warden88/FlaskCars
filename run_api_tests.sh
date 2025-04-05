#!/bin/bash


python app.py &


sleep 5


mkdir -p tests/results

# Запускаем API тесты
pytest -s -v tests/test_app.py > tests/results/api_results.txt
