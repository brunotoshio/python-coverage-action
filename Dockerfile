FROM python:3.6-alpine

COPY ./src/ .

ENTRYPOINT ["python", "main.py"]
