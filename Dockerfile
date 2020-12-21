FROM python:3.8.5-slim

COPY ./src/ .

ENTRYPOINT ['python', 'main.py']
