FROM mcr.microsoft.com/playwright/python:latest

WORKDIR /app


COPY . /app/


RUN chmod +x /app/run_api_tests.sh /app/run_ui_tests.sh


RUN pip install --upgrade pip \
    && pip install -r /app/requirements.txt


RUN playwright install --with-deps
