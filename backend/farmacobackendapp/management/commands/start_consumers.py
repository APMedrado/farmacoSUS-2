from django.core.management.base import BaseCommand
from farmacobackendapp.kafka_consumer import consume_messages

class Command(BaseCommand):
    help = 'Starts multiple Kafka consumers'

    def handle(self, *args, **kwargs):
        topics = ['estoque_local']  # Adicionar mais tópicos aqui conforme necessário
        self.stdout.write(f"Starting consumers for topics: {', '.join(topics)}")
        consume_messages(topics)