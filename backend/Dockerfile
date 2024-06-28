# backend/Dockerfile

FROM python:3.8-slim

# Configura o diretório de trabalho no contêiner
WORKDIR /app

# Copia o requirements.txt para o diretório de trabalho
COPY requirements.txt .

# Instala as dependências
RUN pip install -r requirements.txt

# Copia o conteúdo do diretório atual para o contêiner
COPY . .

# Executa as migrações e inicia o servidor
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]