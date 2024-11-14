from kafka import KafkaConsumer
import json

from consumers.message_consumer import email
from database.postgres_db import db_session

# Kafka consumer setup
consumer = KafkaConsumer(
    'messages.hostage',
    bootstrap_servers=['kafka:9092'],
    auto_offset_reset='earliest',
    group_id='messages',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

for message in consumer:
    email = message.value
    db_session.add(email)
    db_session.commit()
    print(f"Stored suspicious email: {email}")