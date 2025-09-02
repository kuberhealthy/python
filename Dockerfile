FROM python:3.11-alpine

WORKDIR /app
COPY kuberhealthy_client kuberhealthy_client
COPY example example

CMD ["python3", "/app/example/client.py"]
