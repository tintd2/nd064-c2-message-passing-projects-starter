import json
import logging
import os

from kafka import KafkaProducer
from typing import Dict

TOPIC_NAME = os.environ["TOPIC_NAME"]
KAFKA_SERVER = os.environ["KAFKA_SERVER"]
KAFKA_PASSWORD = os.environ["KAFKA_PASSWORD"]

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("udaconnect-location-ingester-service")

# Create the kafka producer
producer = KafkaProducer(
    security_protocol="SASL_PLAINTEXT", 
    sasl_mechanism="SCRAM-SHA-256", 
    sasl_plain_username="user1", 
    sasl_plain_password=KAFKA_PASSWORD, 
    bootstrap_servers=KAFKA_SERVER
)

def send_location(location_data):
    print(f"location_data: {location_data}")
    encoded_data = json.dumps(location_data).encode('utf-8')
    producer.send(TOPIC_NAME, encoded_data)
    producer.flush()
    logger.info(f"Sent to kafka successfully.")