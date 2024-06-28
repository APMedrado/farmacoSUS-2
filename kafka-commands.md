Comandos-exemplo para docker-compose kafka:

* Criar um tópico
```sh
docker-compose exec kafka kafka-topics --create --topic estoque_local --bootstrap-server kafka:9092 --partitions 1 --replication-factor 1
```

* Listar tópicos
```sh
docker-compose exec kafka kafka-topics --list --bootstrap-server kafka:9092
```

* Descrição de um tópico
```sh
docker-compose exec kafka kafka-topics --describe --topic estoque_local --bootstrap-server kafka:9092
```

* Iniciar um produtor (vai ficar aberto esperando inputs)
```sh
docker-compose exec kafka kafka-console-producer --topic estoque_local --bootstrap-server kafka:9092
# Exemplo de input
# > {"nome": "Paracetamol", "quantidade": 100}
```

* Iniciar um consumidor (vai ficar aberto esperando outputs)
```sh
docker-compose exec kafka kafka-console-consumer --topic estoque_local --from-beginning --bootstrap-server kafka:9092
# Vai mostrar os outputs desde o começo e continuar recebendo e mostrando
```