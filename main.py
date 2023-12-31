from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from model import Payload
from datetime import datetime, timedelta, timezone
from metrics import registry, register_enviro_metrics, generate_latest


app = FastAPI()

@app.post("/submit/")
async def submit_readings(payload: Payload):

    td = datetime.now(timezone.utc) - payload.timestamp

    if td > timedelta(minutes=5):
        # too old to care about
        return

    register_enviro_metrics(payload)

    return

@app.get("/metrics/")
async def metrics():
    metrics_string =  generate_latest(registry)
    return PlainTextResponse(content=metrics_string, media_type="text/plain")