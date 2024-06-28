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
            defaults={'quantidade': quantidade}
        )

        if not created:
            estoque_local.quantidade += quantidade
            estoque_local.save()
    except Exception as e:
        print(f'Failed to process message for estoque_local: {e}')
