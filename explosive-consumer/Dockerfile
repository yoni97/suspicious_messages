# Dockerfile

FROM python:3.9-slim

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY . /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

EXPOSE 5002

CMD ["python", "explos_consumer.py"]