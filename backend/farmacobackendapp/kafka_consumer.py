from confluent_kafka import Consumer, KafkaException
import json
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

from .process_estoque_local import process_message_estoque_local

conf = {
    'bootstrap.servers': 'kafka:9092',
    'group.id': 'general_consumer_group',
    'auto.offset.reset': 'earliest',
}

consumer = Consumer(conf)

def consume_messages(topics):
    consumer.subscribe(topics)
    logger.info(f"Subscribed to topics: {', '.join(topics)}")
    try:
        while True:
            msg = consumer.poll(timeout=1.0)
            if msg is None:
                logger.info(f"No messages")
                continue
            if msg.error():
                if msg.error().code() == KafkaException._PARTITION_EOF:
                    logger.info(f"Kafka exception")
                    continue
                else:
                    logger.error(f"Consumer error: {msg.error()}")
                    break

            message = json.loads(msg.value().decode('utf-8'))
            topic = msg.topic()
            print("oi")
            logger.info(f"Consumed message from topic {topic}: {message}")

            if topic == 'estoque_local':
                process_message_estoque_local(message)
            else:
                logger.warning(f"Unknown topic: {topic}")

    except KeyboardInterrupt:
        pass
    finally:
        consumer.close()
        logger.info("Consumer closed")