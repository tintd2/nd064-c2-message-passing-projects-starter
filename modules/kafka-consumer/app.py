import os

from kafka import KafkaConsumer
from services import save_location

TOPIC_NAME = os.environ["TOPIC_NAME"]
KAFKA_SERVER = os.environ["KAFKA_SERVER"]
KAFKA_PASSWORD = os.environ["KAFKA_PASSWORD"]

# Create the kafka consumer
consumer = KafkaConsumer(
    TOPIC_NAME, 
    security_protocol="SASL_PLAINTEXT", 
    sasl_mechanism="SCRAM-SHA-256", 
    sasl_plain_username="user1", 
    sasl_plain_password=KAFKA_PASSWORD, 
    bootstrap_servers=KAFKA_SERVER
)
consumer.poll(timeout_ms=2000)

while True:
    for message in consumer:
        location_data = message.value.decode('utf-8')
        save_location(location_data)