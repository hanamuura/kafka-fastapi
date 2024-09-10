from faststream.kafka.fastapi import KafkaRouter
from enum import Enum
from utils.config import app_config

class Topics(Enum):
    PUBLISH = "test-publish-topic"
    SUBCRIBE = "test-subscribe-topic"

kafka_router = KafkaRouter(
    app_config.kafka.host,
    request_timeout_ms=app_config.kafka.max_timeout,
    schema_url="/kafka",
    include_in_schema=True,
)
