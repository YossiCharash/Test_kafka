import json
from kafka import KafkaProducer


# Kafka producer setup
producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    )

def send_message(email):
    producer.send('all.messages', email)
    print("sent message")
    producer.flush()
    return

