from confluent_kafka import Producer, Consumer

KAFKA_BROKER = 'localhost:9092'
TOPIC = 'novo_topico'  # Tópico exemplo

producer = Producer({
    'bootstrap.servers': KAFKA_BROKER
})

consumer = Consumer({
    'bootstrap.servers': KAFKA_BROKER,
    'group.id': 'grupo_de_consumidores',
    'auto.offset.reset': 'earliest'
})

consumer.subscribe([TOPIC])

def send_message(message):
    producer.produce(TOPIC, message)
    producer.flush()

def consume_messages():
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            print(f"Consumer error: {msg.error()}")
            continue

        print(f"Received message: {msg.value().decode('utf-8')}")
