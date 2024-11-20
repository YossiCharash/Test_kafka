from kafka import KafkaConsumer
import json


from kf.consumers.tabales import  insert_exploie








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

    check_sentences(sentences['sentences'])
    insert_exploie(dict(sentences))
    print(f"Stored high-value transaction: {sentences}")