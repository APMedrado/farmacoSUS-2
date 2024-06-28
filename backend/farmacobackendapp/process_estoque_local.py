from .models import EstoqueLocal, Farmaco, PostoDistribuicao
from .kafka_producer import produce_message

def process_message_estoque_local(message):
    try:
        medicamento_codigo = message['medicamento']
        posto_cnes = message['posto_distribuicao']
        quantidade = message['quantidade']

        medicamento = Farmaco.objects.get(codigo_barra=medicamento_codigo)
        posto_distribuicao = PostoDistribuicao.objects.get(cnes=posto_cnes)

        estoque_local, created = EstoqueLocal.objects.get_or_create(
            medicamento=medicamento,
            posto_distribuicao=posto_distribuicao,
            defaults={'quantidade': 0}  # Define a quantidade inicial como 0 se criado
        )

        if not created:
            # Subtrair a quantidade, garantindo que não fique negativa
            estoque_local.quantidade = max(estoque_local.quantidade - quantidade, 0)
            estoque_local.save()
        else:
            print(f'No existing stock entry found for medicamento {medicamento_codigo} and posto {posto_cnes}. Created new entry with default quantity 0.')

        # Verificar se a quantidade está abaixo de 10 e produzir uma mensagem
        if estoque_local.quantidade < 10:
            low_stock_message = {
                'medicamento': medicamento_codigo,
                'posto_distribuicao': posto_cnes,
                'quantidade': estoque_local.quantidade
            }
            produce_message('low_stock_alert', low_stock_message)
            print(f'Produced low stock alert message: {low_stock_message}')

    except Exception as e:
        print(f'Failed to process message for estoque_local: {e}')