FROM python:3.11-alpine

WORKDIR /app
COPY kuberhealthy_client kuberhealthy_client
COPY client.py .

CMD ["python3", "/app/client.py"]
