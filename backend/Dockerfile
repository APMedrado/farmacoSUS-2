FROM python:3.8-slim

# Configura o diretório de trabalho no contêiner
WORKDIR /app

# Copia o requirements.txt para o diretório de trabalho
COPY requirements.txt .

# Instala as dependências
RUN pip install -r requirements.txt



# Copia o conteúdo do diretório atual para o contêiner
COPY . .

ENV DJANGO_SETTINGS_MODULE=farmacobackend.settings

# Executa as migrações e inicia o servidor
CMD ["sh", "-c", "python manage.py runserver 0.0.0.0:8000 & python /app/farmacobackendapp/consumers/consume_deliveries.py"]