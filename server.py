# -*- coding: utf-8 -*-

"""
Author: Causa Efeito
Date: 2022/03
"""

from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS


class Sensor(BaseModel):
    name: str
    value: float
    value2: Optional[float] = None
    description: Optional[str] = None


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/api/v1/sensor")
async def create_item(sensor: Sensor) -> str:

    data = sensor.dict()
    print(f"post data: {data}")

    return "ok"


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
