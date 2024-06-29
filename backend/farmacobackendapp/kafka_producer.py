from confluent_kafka import Producer
import json

conf = {
    'bootstrap.servers': 'kafka:9092',
}

producer = Producer(**conf)

def delivery_report(err, msg):
    if err is not None:
        print(f'Message delivery failed: {err}')
    else:
        print(f'Message delivered to {msg.topic()} [{msg.partition()}]')


# Função que envia uma mensagem para um tópico 
def produce_message(topic, message):
    try:
        print(f'Producing message to topic {topic}: {message}')
        producer.produce(topic, json.dumps(message).encode('utf-8'), callback=delivery_report)
        producer.poll(0)
    except Exception as e:
        print(f'Failed to produce message: {e}')

# Flush producer to ensure delivery
producer.flush()