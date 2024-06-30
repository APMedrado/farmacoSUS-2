#!/bin/bash

# Espera pelo Kafka estar pronto
while ! nc -z kafka 9092; do   
  sleep 0.1 
done

# Cria os tópicos necessários
kafka-topics --create --topic estoque_local --bootstrap-server kafka:9092 --partitions 1 --replication-factor 1
kafka-topics --create --topic low_stock_alert --bootstrap-server kafka:9092 --partitions 1 --replication-factor 1
kafka-topics --create --topic abastecimento_alert --bootstrap-server kafka:9092 --partitions 1 --replication-factor 1
kafka-topics --create --topic regional_supplying_actions --bootstrap-server kafka:9092 --partitions 1 --replication-factor 1

# Espera para garantir que os tópicos estejam prontos
sleep 5
