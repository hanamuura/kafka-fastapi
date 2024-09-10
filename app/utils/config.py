import os
from dotenv import load_dotenv
from dataclasses import dataclass


env = load_dotenv()

@dataclass
class KafkaConfig:
    host: str
    max_timeout: int

@dataclass
class AppConfig:
    kafka: KafkaConfig


kafka_host = os.getenv("KAFKA_URL")

assert kafka_host

kafka_config = KafkaConfig(
    host=kafka_host,
    max_timeout=400
)


app_config = AppConfig(
    kafka=kafka_config
)
