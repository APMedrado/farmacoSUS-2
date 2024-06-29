from .models import EstoqueLocal, Farmaco, PostoDistribuicao
from .kafka_producer import produce_message

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def process_message_estoque_local(message):
    try:
        medicamento_codigo = message['medicamento']
        posto_cnes = message['posto_distribuicao']
        quantidade = message['quantidade']

        medicamento = Farmaco.objects.get(codigo_barra=medicamento_codigo)
        posto_distribuicao = PostoDistribuicao.objects.get(cnes=posto_cnes)
        
        estoque_local = EstoqueLocal.objects(
            medicamento=medicamento,
            posto_distribuicao=posto_distribuicao
        ).first()
    
        if estoque_local:
            estoque_local.quantidade = max(estoque_local.quantidade - quantidade, 0)
            estoque_local.save()
        else :
            logger.error(f'No existing stock entry found for medicamento {medicamento_codigo} and posto {posto_cnes}.')
        
        logger.info(f'quantidade apos retirada: {estoque_local.quantidade}')    
        # Verificar se a quantidade está abaixo de 10 e produzir uma mensagem
        if estoque_local.quantidade < 15:
            low_stock_message = {
                'medicamento': medicamento_codigo,
                'posto_distribuicao': posto_cnes,
                'quantidade': estoque_local.quantidade
            }
            produce_message('low_stock_alert', low_stock_message)
            (f'Produced low stock alert message: {low_stock_message}')

    except Exception as e:
        logger.error(f'Failed to process message for estoque_local: {e}')