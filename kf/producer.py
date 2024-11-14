import json
from kafka import KafkaProducer


# Kafka producer setup
producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def if_is(body, parameter):
    is_true = [i for i in body if any(parameter == j for j in i.split(' '))]
    if len(is_true) > 0:
         return True
    else:
        return False


def email_check(email):
    message_body = email['sentences']
    hostage = if_is(message_body, 'hostage')
    explos = if_is(message_body, 'explores')
    if hostage:
        producer.send("hostage.messages", value=message_body)
        print("the hostage is sender")
    if explos:
        producer.send("explosive.messages", value=message_body)
        print("the explos is sender")




def send_message(email):
    producer.send('all.messages', value=email)
    print("sent message to all messages")
    email_check(email)
    producer.flush()
    return

