from flask import Blueprint, request
from kafka import KafkaProducer
import json

suspicious_email_bp = Blueprint('suspicious_email', __name__)

producer = KafkaProducer(
    bootstrap_servers=['kafka:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

@suspicious_email_bp.route('/api/email', methods=['POST'])
def get_email():
    data = request.get_json()
    producer.send('get_email', value=data)





