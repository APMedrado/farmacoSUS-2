from confluent_kafka import Producer, Consumer, KafkaException
#from confluent_kafka.admin import KafkaAdminClient, NewTopic
import logging
import json

KAFKA_BROKER = 'kafka:9092'

# Configuração do produtor
producer_conf = {
    'bootstrap.servers': KAFKA_BROKER
}
producer = Producer(producer_conf)

# Configuração do consumidor
consumer_conf = {
    'bootstrap.servers': KAFKA_BROKER,
    'group.id': 'delivery_group',
    'auto.offset.reset': 'earliest'
}
consumer = Consumer(consumer_conf)

def delivery_callback(err, msg):
    if err:
        logging.error(f'Failed to deliver message: {err}')
    else:
        logging.info(f'Message produced: {msg.topic()} [{msg.partition()}] at offset {msg.offset()}')

def send_delivery_message(message):
    producer.produce('deliveries', key=str(message['id']), value=json.dumps(message), callback=delivery_callback)
    producer.flush()

def consume_delivery_messages(process_message_callback):
    try:
        while True:
            msg = consumer.poll(1.0)
            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaException._PARTITION_EOF:
                    continue
                else:
                    logging.error(msg.error())
                    break

            process_message_callback(json.loads(msg.value().decode('utf-8')))

    except KeyboardInterrupt:
        pass
    finally:
        consumer.close()

def create_topic(topic_name):
    admin_client = KafkaAdminClient(bootstrap_servers=KAFKA_BROKER)
    topic_list = [NewTopic(name=topic_name, num_partitions=1, replication_factor=1)]
    try:
        admin_client.create_topics(new_topics=topic_list, validate_only=False)
        logging.info(f'Topic "{topic_name}" created successfully.')
    except KafkaException as e:
        logging.error(f'Error creating topic "{topic_name}": {e}')
    finally:
        admin_client.close()