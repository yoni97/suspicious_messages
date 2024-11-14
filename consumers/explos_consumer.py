from kafka import KafkaConsumer
import json
from database.postgres_db import db_session

consumer = KafkaConsumer(
    'messages.explosive',
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