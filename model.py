from pydantic import BaseModel
from datetime import datetime

class Readings(BaseModel):
    pressure: float
    temperature: float
    color_temperature: int
    gas_resistance: int
    aqi: float
    humidity: float
    luminance: int

class Payload(BaseModel):
    readings: Readings
    nickname: str
    model: str
    uid: str
    timestamp: datetime