from fastapi import APIRouter
from app.dto.kafka import WriteHuman
from app.handlers import urls
from utils.kafka import kafka_router, Topics


class TestController:
    router: APIRouter

    def __init__(self, router: APIRouter):
        self.router = router
        self.router.add_api_route(
            path=urls.TEST_PUBLISH,
            endpoint=self.publish_handler,
            methods=["POST"]
        )

    async def publish_handler(self, human: WriteHuman) -> None:
        await kafka_router.broker.publish(
            message=human,
            topic=Topics.PUBLISH.value
        )
