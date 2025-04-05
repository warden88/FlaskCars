FROM mcr.microsoft.com/playwright/python:latest

WORKDIR /app

# Копируем весь проект
COPY . /app/

RUN ls -l /app

# Устанавливаем разрешения на выполнение для скриптов
RUN chmod +x /app/run_api_tests.sh /app/run_ui_tests.sh

# Устанавливаем зависимости
RUN pip install --upgrade pip \
    && pip install -r /app/requirements.txt

# Устанавливаем Playwright с зависимостями
RUN playwright install --with-deps
