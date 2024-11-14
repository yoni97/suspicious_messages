from collections import Counter

from flask import Blueprint, request, jsonify
from kafka import KafkaProducer
import json

from models.email import EmailModel

suspicious_email_bp = Blueprint('suspicious_email', __name__)

producer = KafkaProducer(
    bootstrap_servers=['kafka:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

@suspicious_email_bp.route('/api/email', methods=['POST'])
def get_email():
    data = request.get_json()
    producer.send("messages.all", value=data)
    if not data:
        return jsonify({"error": "Invalid data"}), 400

    producer.send('get_email', value=data)
    print(f"Sent {data} to messages.all")

    send_to_topic_based_on_keywords(data)

    return jsonify({"message": "Email received and processed"}), 200

def send_to_topic_based_on_keywords(email_data):
    sentences = email_data.get("sentences", [])

    for sentence in sentences:
        for keyword, topic in KEYWORDS.items():
            if keyword in sentence.lower():
                producer.send(topic, value=email_data)
                print(f"Sent to {topic} due to keyword: {keyword}")
                break


@suspicious_email_bp.route('/api/suspicious_content', methods=['GET'])
def get_suspicious_content():
    email = request.args.get('email')

    if not email:
        return jsonify({"error": "Email parameter is required"}), 400

    # שליפת כל התוכן החשוד עבור אימייל מסוים
    hostage_content = EmailModel.query.filter_by(email=email).all()
    explosive_content = EmailModel.query.filter_by(email=email).all()

    # איחוד התוכן החשוד
    suspicious_content = [
                             {"type": "hostage", "sentence": content.sentence, "detected_at": content.detected_at}
                             for content in hostage_content
                         ] + [
                             {"type": "explosive", "sentence": content.sentence, "detected_at": content.detected_at}
                             for content in explosive_content
                         ]

    return jsonify({"email": email, "suspicious_content": suspicious_content}), 200





@suspicious_email_bp.route('/api/most_common_word', methods=['GET'])
def get_most_common_word():
    email = request.args.get('email')

    if not email:
        return jsonify({"error": "Email parameter is required"}), 400

    hostage_sentences = EmailModel.query.with_entities(EmailModel.sentence).filter_by(
        email=email).all()
    explosive_sentences = EmailModel.query.with_entities(EmailModel.sentence).filter_by(
        email=email).all()

    all_sentences = [sentence[0] for sentence in hostage_sentences + explosive_sentences]

    word_counter = Counter()
    for sentence in all_sentences:
        words = sentence.lower().split()
        word_counter.update(words)

    # מציאת המילה הנפוצה ביותר
    if word_counter:
        most_common_word, count = word_counter.most_common(1)[0]
    else:
        return jsonify({"error": "No suspicious content found for the provided email"}), 404

    return jsonify({
        "email": email,
        "most_common_word": most_common_word,
        "occurrences": count
    }), 200