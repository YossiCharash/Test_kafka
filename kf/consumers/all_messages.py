from kafka import KafkaConsumer
import json
from pymongo import MongoClient

# MongoDB setup
client = MongoClient('mongodb://localhost:27017')
db = client['suspicious_emails']
collection = db['all_email']



# Kafka consumer setup
consumer = KafkaConsumer(
    'all.messages',
    bootstrap_servers="localhost:9092",
    auto_offset_reset='earliest',
    group_id='all.messages',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

for message in consumer:
    transaction = message.value
    print("the message is com")
    collection.insert_one(transaction)
    print(f"Stored high-value transaction: {transaction}")