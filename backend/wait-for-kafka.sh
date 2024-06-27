#!/bin/sh

# Aguardando o Kafka estar disponível
while ! nc -z kafka 9092; do   
  echo "Aguardando Kafka..."
  sleep 1
done

exec "$@"