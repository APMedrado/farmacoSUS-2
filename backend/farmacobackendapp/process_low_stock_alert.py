from .models import EstoqueLocal, Farmaco, PostoDistribuicao, LowStockAlert
import logging

# Configurar o logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def send_notification(message):
    # Implemente aqui o envio de notificação (e-mail, SMS, etc.)
    logger.info(f"Notification sent for low stock: {message}")

def log_low_stock_alert(medicamento, posto_distribuicao, quantidade, status):
    # Registrar o alerta de baixo estoque no banco de dados
    
    alert = LowStockAlert.objects.get(medicamento = medicamento, posto_distribuicao = posto_distribuicao)
    if alert:
        alert.quantidade =  quantidade
        alert.status = status   
    else: 
        alert = LowStockAlert(
            medicamento=medicamento,
            posto_distribuicao =posto_distribuicao,
            quantidade = quantidade,
            status = status
        )
    alert.save()
    logger.info(f"Low stock alert logged: {alert}")

def process_message_low_stock_alert(message):
    try:
        medicamento_codigo = message['medicamento']
        posto_cnes = message['posto_distribuicao']
        quantidade = message['quantidade']

        medicamento = Farmaco.objects.get(codigo_barra=medicamento_codigo)
        posto_distribuicao = PostoDistribuicao.objects.get(cnes=posto_cnes)
        
        status = get_status(quantidade)
        # Enviar notificação
        if status == 'out of stock':
            send_notification(message)

        # Registrar o alerta no banco de dados
        log_low_stock_alert(medicamento, posto_distribuicao, quantidade, status)

    except Exception as e:
        logger.error(f'Failed to process low stock alert message: {e}')
        
def get_status(quant) -> str:
    if quant < 10:
        return 'low'
    elif quant < 5:
        return 'critical'
    elif quant == 0:
        return 'out of stock'
    return 'attention'