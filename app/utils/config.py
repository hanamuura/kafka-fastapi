import os
from dotenv import load_dotenv
from dataclasses import dataclass
from typing import Literal


env = load_dotenv()

@dataclass
class KafkaConfig:
    host: str
    max_timeout: int
    schema_url: str
    include_in_schema: bool
    acks: Literal[0, 1, -1, "all"]

@dataclass
class AppConfig:
    kafka: KafkaConfig


kafka_host = os.getenv("KAFKA_URL")

assert kafka_host

kafka_config = KafkaConfig(
    host=kafka_host,
    max_timeout=400,
    schema_url="/kafka",
    include_in_schema=True,
    acks="all"
)


app_config = AppConfig(
    kafka=kafka_config
)
