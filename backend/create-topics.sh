#!/bin/bash

# Espera pelo Kafka estar pronto
while ! nc -z kafka 9092; do   
  sleep 0.1 
done

# Cria os tópicos necessários

kafka-topics --create --topic estoque_local --bootstrap-server kafka:9092 --partitions 1 --replication-factor 1
# ...
