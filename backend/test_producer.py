import json
from farmacobackendapp.kafka_producer import produce_message

def test_produce():
    # Mensagem de teste arbitrária
    message = {
        'medicamento': '7891011121314',
        'posto_distribuicao': '1234567',
        'quantidade': 10
    }
    
    print(f"Producing test message: {message}")
    produce_message('estoque_local', message)

if __name__ == "__main__":
    test_produce()