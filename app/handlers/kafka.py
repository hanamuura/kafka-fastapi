import asyncio
from utils.kafka import kafka_router, Topics
from dto.kafka import ReadHuman, WriteHuman


@kafka_router.subscriber(Topics.SUBCRIBE.value)
@kafka_router.publisher(Topics.PUBLISH.value)
async def first_handler(
    human: ReadHuman
) -> WriteHuman:
    await asyncio.sleep(10)
    return WriteHuman(
        name=human.name,
        age=human.age
    )

@kafka_router.publisher(Topics.SUBCRIBE.value)
@kafka_router.subscriber(Topics.PUBLISH.value)
async def second_handler(
    human: ReadHuman
) -> WriteHuman:
    await asyncio.sleep(10)
    return WriteHuman(
        name=human.name,
        age=human.age
    )
