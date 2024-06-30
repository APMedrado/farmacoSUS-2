from .models import NotificacaoAbastecimento
from django.core.mail import send_mail
from .kafka_producer import produce_message




def process_notify_email(message):
    print(message)
    subject = "[Teste] "
    content = "Oi, toinho. Ta funcionando"
    from_email = "gatinhasfrancesas@gmail.com" 
    recipient_list = ["apmedrado@usp.br", "lucas.hsantanna@gmail.com"]
    send_mail(subject, content, from_email, recipient_list)