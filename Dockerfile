FROM python:3.8.5-slim

COPY ./src/ .

RUN pip install

ENTRYPOINT ['python', 'main.py']
