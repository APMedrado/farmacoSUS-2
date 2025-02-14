from confluent_kafka import Consumer, KafkaError
import json
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
from .process_notify_email import process_notify_email
from .process_estoque_local import process_message_estoque_local
from .process_low_stock_alert import process_message_low_stock_alert
from .process_regional_supplying_actions import process_message_regional_supplying_actions

conf = {
    'bootstrap.servers': 'kafka:9092',
    'group.id': 'general_consumer_group',
    'auto.offset.reset': 'earliest',
}

consumer = Consumer(conf)


# Função que consome uma mensagem de um tópico
# A depender do tópico, envia a mensagem para ser processada de forma própria (process_)
def consume_messages(topics):
    consumer.subscribe(topics)
    logger.info(f"Subscribed to topics: {', '.join(topics)}")
    try:
        while True:
            msg = consumer.poll(timeout=1.0)
            if msg is None:
                continue
            if msg.error():
                error_code = msg.error().code()
                if error_code == KafkaError._PARTITION_EOF:
                    logger.info("End of partition reached")
                    continue
                else:
                    logger.error(f"Consumer error: {msg.error()}")
                    break

            message = json.loads(msg.value().decode('utf-8'))
            topic = msg.topic()
            
            logger.info(f"Consumed message from topic {topic}: {message}")

            if topic == 'estoque_local':

                process_message_estoque_local(message)
            elif topic == 'low_stock_alert':
                process_message_low_stock_alert(message)
            elif topic == 'abastecimento_alert':
                process_notify_email(message)
            elif topic == 'regional_supplying_actions':
                process_message_regional_supplying_actions(message)
            else:
                logger.warning(f"Unknown topic: {topic}")


    except KeyboardInterrupt:
        pass
    finally:
        consumer.close()
        logger.info("Consumer closed")