Este projeto foi desenvolvido para a disciplina SSC0904 - Sistemas Computacionais Distribuídos (2024) do Bacharelado em Ciências de Computação na USP.

## Requisitos

Para executar o projeto, é necessário ter o Node 18.18.0, o Docker e o Docker Compose instalados na sua máquina. 

## Instruções de Execução em Ambiente Remoto

Essas instruções supôem utilização em máquina remota, lá a aplicação já deve estar em exeução. Como há problemas para execução remota do frontend, é necessário executá-lo localmente. Após acessar o endereço remoto, execute os seguintes passos:

1. Clone o repositório para a sua máquina local:
    ```sh
    git clone <url-do-repositorio>
    cd farmacosus-2
    ```

2. Como há problemas para execução remota do frontend, é necessário executá-lo localmente:
    ```sh
    cd frontend
    npm run dev
    ```

## Instruções de Execução na Máquina Local

Essas instruções supôem que os endereços nas aplicações estão configurados para sua máquina local. Eles não estão por padrão.

1. Clone o repositório para a sua máquina local:
    ```sh
    git clone <url-do-repositorio>
    cd farmacosus-2
    ```

2. Execute o seguinte comando para construir e iniciar os contêineres em segundo plano:
    ```sh
    docker-compose up --build -d
    ```

Isso irá iniciar todos os serviços necessários para o funcionamento do sistema.
