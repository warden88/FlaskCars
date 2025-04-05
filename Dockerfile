# Используем официальный образ Python
FROM mcr.microsoft.com/playwright/python:v1.43.1-jammy

# Установка зависимостей
WORKDIR /app
COPY . /app

RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# # Установка браузеров Playwright (если нужно вручную)
# RUN playwright install chromium



