import json
from kafka import KafkaConsumer, KafkaProducer

consumer = KafkaConsumer(
    'get_email',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    group_id='transactions',
    enable_auto_commit=True,
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

producer = KafkaProducer(bootstrap_servers='localhost:9092',
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

for message in consumer:
    decoded_message = message.value['sentences']
    for sentence in decoded_message:
        if 'explos' in decoded_message[sentence]:
            producer.send('messages.explosive', value=decoded_message)

        if 'hostage' in decoded_message[sentence]:
            producer.send('messages.hostage', value=decoded_message)

        producer.send('messages.all', value=decoded_message)
        print(f'Email {decoded_message} is  sent!')

producer.flush()
producer.close()