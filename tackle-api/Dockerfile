FROM python:3.9.4

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY server.py .
COPY db_config.py .
COPY config.py .
COPY models.py .
COPY util.py .
COPY routes.py .
COPY functional_tests functional_tests

ENV FLASK_APP server.py
