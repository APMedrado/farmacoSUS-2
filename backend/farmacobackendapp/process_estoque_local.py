from .models import EstoqueLocal, Farmaco, PostoDistribuicao

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

    except Exception as e:
        print(f'Failed to process message for estoque_local: {e}')