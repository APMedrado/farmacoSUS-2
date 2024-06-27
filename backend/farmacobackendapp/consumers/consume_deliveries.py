import os
import sys
import django
import json
import logging

# Adicione o diretório /app ao caminho do Python
sys.path.append('/app')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'farmacobackend.settings')
django.setup()

from farmacobackendapp.models import EstoqueLocal, Farmaco, PostoDistribuicao
from farmacobackendapp.kafka_config import consume_delivery_messages

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def process_delivery_message(data):
    try:
        posto_cnes = data['posto_distribuicao']
        medicamentos = data['medicamentos']

        posto = PostoDistribuicao.objects.get(cnes=posto_cnes)
        for med in medicamentos:
            medicamento = Farmaco.objects.get(codigo_barra=med['codigo_barra'])
            estoque_local = EstoqueLocal.objects.get(medicamento=medicamento, posto_distribuicao=posto)
            estoque_local.quantidade -= med['quantidade']
            estoque_local.save()
    except Exception as e:
        logger.error(f'Erro ao processar mensagem de entrega: {e}')

if __name__ == '__main__':
    logger.info('Iniciando o consumidor de mensagens')
    consume_delivery_messages(process_delivery_message)