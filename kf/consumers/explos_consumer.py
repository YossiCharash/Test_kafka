from kafka import KafkaConsumer
import json

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker



connection_url = "postgresql://yossi:8520@localhost:5432/Suspicious_emails"
engine = create_engine(connection_url)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
# Kafka consumer setup
consumer = KafkaConsumer(
    'explosive.messages',
    bootstrap_servers="localhost:9092",
    auto_offset_reset='earliest',
    group_id='all.messages',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

def check_sentences(sentences):
    ind = 0
    for i,w in enumerate(sentences):
        if "explos" in w:
            sentences[ind] = w
            print(sentences)



for message in consumer:
    sentences = message.value
    print("the message is com")
    check_sentences(sentences)
    # db_session.add(sentences)
    print(f"Stored high-value transaction: {sentences}")