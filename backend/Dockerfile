FROM python:3.8-slim

# Configura o diretório de trabalho no contêiner
WORKDIR /app

# Copia o requirements.txt para o diretório de trabalho
COPY requirements.txt .

# Instala as dependências do Python
RUN pip install -r requirements.txt

# Instala o netcat-openbsd
RUN apt-get update && apt-get install -y netcat-openbsd

# Copia o conteúdo do diretório atual para o contêiner
COPY . .

# Copia o script de espera
COPY wait-for-kafka.sh .

# Torna o script executável
RUN chmod +x wait-for-kafka.sh

ENV DJANGO_SETTINGS_MODULE=farmacobackend.settings

# Executa as migrações e inicia o servidor
CMD ["sh", "-c", "./wait-for-kafka.sh python manage.py runserver 0.0.0.0:8000 & python /app/farmacobackendapp/consumers/consume_deliveries.py"]