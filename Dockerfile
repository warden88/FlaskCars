FROM mcr.microsoft.com/playwright/python:latest

WORKDIR /app
COPY . /app


COPY run_api_tests.sh /run_api_tests.sh
COPY run_ui_tests.sh /run_ui_tests.sh
RUN chmod +x /run_api_tests.sh /run_ui_tests.sh


RUN pip install --upgrade pip \
    && pip install -r requirements.txt


RUN playwright install --with-deps
