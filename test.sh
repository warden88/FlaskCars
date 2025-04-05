#!/bin/bash

# Запуск Flask в фоне
python app.py &

# Ждём, пока Flask поднимется   
sleep 3

# Запускаем API тесты
pytest -s -v tests/test_app.py

# Запускаем UI тесты
pytest -s -v tests/test_ui.py
