FROM openjdk:11-jre-slim

COPY kafka_2.13-3.5.0 kafka

RUN KAFKA_CLUSTER_ID="$(kafka/bin/kafka-storage.sh random-uuid)"; \
    kafka/bin/kafka-storage.sh format -t yux_DscfTfSP1LiU9IkpJB -c kafka/config/kraft/server.properties;

VOLUME ["/kafka"]

EXPOSE 9092

CMD ["kafka/bin/kafka-server-start.sh", "kafka/config/kraft/server.properties"]