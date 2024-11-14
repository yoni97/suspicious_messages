import json
from kafka import KafkaConsumer, KafkaProducer

consumer = KafkaConsumer(
    'get_email',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    group_id='emails',
    enable_auto_commit=True,
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

producer = KafkaProducer(bootstrap_servers='localhost:9092',
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

for message in consumer:
    decoded_message = message.value['sentences']
    sorted_list_by_danger = []
    for sentence in decoded_message:
        if 'explos' in decoded_message[sentence]:
            sorted_list_by_danger.append(sentence)
            producer.send('messages.explosive', value=sentence)

        if 'hostage' in decoded_message[sentence]:
            sorted_list_by_danger.append(sentence)
            producer.send('messages.hostage', value=sentence)

        print(f'Email {sentence} is  sent!')

producer.flush()
producer.close()