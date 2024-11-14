```bash
cd .\practic\
```

```bash
.venv\Scripts\activate
```

```bash
pip install kafka-python
```

```bash
docker-compose up -d
```

 - access the kafka container (change to the current container name)
```bash
docker exec -it test_kafka-kafka-1 bash
```

 - create the topic all.messages(change to the current topic name)
```bash
kafka-topics --create --topic all.messages-topic --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1
```

- create the topic  messages.hostage(change to the current topic name)

```bash
kafka-topics --create --topic  messages.hostage-topic --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1
```

- create the topic messages.explosive(change to the current topic name)

```bash
kafka-topics --create --topic messages.explosive-topic --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1
```

### how do i know what topics do i have?
```bash
kafka-topics --list --bootstrap-server localhost:9092
```


```bash
python str_consumer.py
```