from fastapi import FastAPI
from utils.kafka import kafka_router


app = FastAPI()
app.include_router(router=kafka_router)
