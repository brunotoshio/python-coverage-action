FROM python:3.6-alpine

COPY ./src/ ./action/

ENTRYPOINT ["python", "action/main.py"]
