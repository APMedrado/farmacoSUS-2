# Use a imagem Node.js como base
FROM node:latest

# Defina o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia os arquivos de package.json e package-lock.json para o diretório de trabalho
COPY package*.json ./

# Instala as dependências do projeto
RUN npm install

# Copia o conteúdo do diretório atual para o contêiner
COPY . .

# Expõe a porta onde o aplicativo Vue.js será executado
EXPOSE 5173

# Comando padrão para iniciar o servidor de desenvolvimento
CMD ["npm", "run", "dev"]