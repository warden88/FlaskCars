#!/bin/bash

# Запуск Flask-приложения в фоновом режиме
python app.py &

# Проверяем, что сервер Flask готов к работе (ожидание доступности порта 5000)
while ! nc -z localhost 5000; do   
  sleep 1
done

# Создаем директорию для хранения результатов
mkdir -p tests/results

# Запуск тестов с сохранением результатов в файл
pytest -s -v tests/test_list_cars_ui.py > tests/results/ui_results.txt
