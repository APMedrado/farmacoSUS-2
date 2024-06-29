from django.core.management.base import BaseCommand
from farmacobackendapp.kafka_consumer import consume_messages
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'Starts multiple Kafka consumers'

    def handle(self, *args, **kwargs):
        topics = ['estoque_local', 'low_stock_alert', 'abastecimento_alert']  # Adicionar mais tópicos aqui conforme necessário
        self.stdout.write(f"Starting consumers for topics: {', '.join(topics)}")
        logger.info(f"Starting consumers for topics: {', '.join(topics)}")
        consume_messages(topics)    