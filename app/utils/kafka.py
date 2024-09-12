from faststream.kafka.fastapi import KafkaRouter
from utils.config import app_config

class Topics:
    PUBLISH = "test-publish-topic"
    SUBCRIBE = "test-subscribe-topic"

kafka_router = KafkaRouter(
    app_config.kafka.host,
    request_timeout_ms=app_config.kafka.max_timeout,
    schema_url=app_config.kafka.schema_url,
    include_in_schema=app_config.kafka.include_in_schema,
    acks=app_config.kafka.acks,
)
