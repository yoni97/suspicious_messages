from kafka import KafkaConsumer
import json
from database.mongo_db import collection

# Kafka consumer setup
consumer = KafkaConsumer(
    'messages.explosive',
    bootstrap_servers=['kafka:9092'],
    auto_offset_reset='earliest',
    group_id='messages',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

for message in consumer:
    email = message.value
    collection.insert_one(email)

    print(f"Stored suspicious email: {email}")