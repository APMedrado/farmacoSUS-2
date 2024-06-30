from .models import EstoqueLocal, Farmaco, PostoDistribuicao
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def process_message_regional_supplying_actions(message):
    try:
        medicamento_codigo = message['medicamento_codigo']
        posto_cnes = message['posto_cnes']
        quantidade = message['quantidade']

        medicamento = Farmaco.objects.get(codigo_barra=medicamento_codigo)
        posto_distribuicao = PostoDistribuicao.objects.get(cnes=posto_cnes)
        
        estoque_local = EstoqueLocal.objects.get(
            medicamento=medicamento,
            posto_distribuicao=posto_distribuicao,
        )
        if estoque_local:
            estoque_local.quantidade_a_receber += quantidade
        else:
            estoque_local = EstoqueLocal(
                medicamento=medicamento,
                posto_distribuicao=posto_distribuicao,
                quantidade=0,
                quantidade_a_receber=quantidade
            )
        estoque_local.save()
        
        logger.info(f'Updated quantidade_a_receber for medicamento {medicamento_codigo} at posto {posto_cnes}: {estoque_local.quantidade_a_receber}')

    except Exception as e:
        logger.error(f'Failed to process message for regional_supplying_actions: {e}')