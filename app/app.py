from fastapi import FastAPI
from utils.kafka import kafka_router
from handlers import new_rest_controller


app = FastAPI()
app.include_router(router=kafka_router)
app.include_router(new_rest_controller().router)
