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

# influx interface class
class SensorData(object):
    def __init__(self, bucket, org, token):
        self.bucket = bucket
        self.token = token
        self.org = org

        self.client = InfluxDBClient(url="http://localhost:8086", token=token, org=org)
        self.write_api = self.client.write_api(write_options=SYNCHRONOUS)
        self.query_api = self.client.query_api()

    def write(self, point):
        # p = Point("my_measurement").tag("location", "Prague").field("temp", 25.3)
        # write_api.write(bucket=bucket, record=p)

        self.write_api.write(bucket=self.bucket, record=point)

    def query(self, query):
        return self.query_api.query(query)

    def get_last_point(self, measurement, tag_key, tag_value):
        query = f"select * from {measurement} where {tag_key} = '{tag_value}' order by time desc limit 1"
        return self.query(query)

    def query_csv(self, query):
        # query_csv('from(bucket:"my-bucket") |> range(start: -10m)')
        return self.query_api.query_csv(query)


class Sensor(BaseModel):
    name: str
    value: float
    value2: Optional[float] = None
    description: Optional[str] = None


app = FastAPI()


INFLUXDB_BUCKET = "causa_efeito"
INFLUXDB_ORG = "causa_efeito"

influx = SensorData(bucket=INFLUXDB_BUCKET, org=INFLUXDB_ORG)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/api/v1/sensor")
async def create_item(sensor: Sensor) -> str:

    data = sensor.dict()
    print(f"post data: {data}")

    p = (
        Point("metric")
        .tag("sensor", data["name"])
        .field("sensor1", data["sensor1"])
        .field("sensor1", data["sensor2"])
        .field("time_precision", "ms")
    )
    influx.write(p)

    return "ok"


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
