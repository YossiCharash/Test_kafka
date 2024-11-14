from kafka import KafkaConsumer
import json
from sqlalchemy.orm import declarative_base

# from kf.consumers.tabales import insert_hostage

Base = declarative_base()

# Kafka consumer setup
consumer = KafkaConsumer(
    'hostage.messages',
    bootstrap_servers="localhost:9092",
    auto_offset_reset='earliest',
    group_id='all.messages',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)





def check_sentence(sentences):
    ind = 0
    new_sentences = []
    for i,w in enumerate(sentences):
        if "hostage" in w.split(' '):
            sentences[ind] = w
            print(sentences)
            new_sentences.append(w)




for message in consumer:
    sentences = message.value
    print("the message is com")
    check_sentence(sentences['sentences'])
    # insert_hostage(sentences)
    print(f"Stored high-value transaction: {sentences}")