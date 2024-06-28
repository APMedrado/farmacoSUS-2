from confluent_kafka import Consumer, KafkaException
import json

from .process_estoque_local import process_message_estoque_local

conf = {
    'bootstrap.servers': 'kafka:9092',
    'group.id': 'general_consumer_group',
    'auto.offset.reset': 'earliest',
    'enable.auto.commit': True,
    'session.timeout.ms': 10000,  # Ajuste de tempo limite de sessão
    'max.poll.interval.ms': 1000000,  # Ajuste máximo do intervalo de enquete
    'heartbeat.interval.ms': 10000
}

consumer = Consumer(conf)

def consume_messages(topics):
    consumer.subscribe(topics)

    try:
        while True:
            msg = consumer.poll(timeout=1.0)
            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaException._PARTITION_EOF:
                    continue
                else:
                    print(msg.error())
                    break

            message = json.loads(msg.value().decode('utf-8'))
            topic = msg.topic()

            print(f'Recebida mensagem em {topic}: {message}') # Debugging

            if topic == 'estoque_local':
                process_message_estoque_local(message)
            # elif topic == 'outro_topico':
                # processar com outro topico
            else:
                print(f"Unknown topic: {topic}")

    except KeyboardInterrupt:
        pass
    finally:
        consumer.close()