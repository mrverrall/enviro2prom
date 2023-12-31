from prometheus_client import Gauge, CollectorRegistry
from prometheus_client.exposition import generate_latest
from model import Payload

registry = CollectorRegistry()

enviro_pressure = Gauge(
    'enviro_pressure',
    'enviro pressure sensor data',
    ['sensor', 'uid'],
    registry=registry)

enviro_temperature = Gauge(
    'enviro_temperature',
    'enviro temerature sensor degrees celcius',
    ['sensor', 'uid'],
    registry=registry)

enviro_color_temperature = Gauge(
    'enviro_color_temperature',
    'enviro light color sensor data',
    ['sensor', 'uid'],
    registry=registry)

enviro_gas_resistance = Gauge(
    'enviro_gas_resistance',
    'enviro gas resistance sensor data ',
    ['sensor', 'uid'],
    registry=registry)

enviro_aqi = Gauge(
    'enviro_aqi',
    'enviro air quality data (gas resistance vs humidity) ',
    ['sensor', 'uid'],
    registry=registry)

enviro_humidity = Gauge(
    'enviro_humidity',
    'enviro humidity sensor data %',
    ['sensor', 'uid'],
    registry=registry)

enviro_luminance = Gauge(
    'enviro_luminance',
    'enviro light sensor data luminance',
    ['sensor', 'uid'],
    registry=registry)

def register_enviro_metrics(payload: Payload):

        readings = payload.readings

        enviro_pressure.labels(payload.nickname, payload.uid).set(readings.pressure)
        enviro_color_temperature.labels(payload.nickname, payload.uid).set(readings.color_temperature)
        enviro_temperature.labels(payload.nickname, payload.uid).set(readings.temperature)
        enviro_humidity.labels(payload.nickname, payload.uid).set(readings.humidity)
        enviro_gas_resistance.labels(payload.nickname, payload.uid).set(readings.gas_resistance)
        enviro_aqi.labels(payload.nickname, payload.uid).set(readings.aqi)
        enviro_luminance.labels(payload.nickname, payload.uid).set(readings.luminance)
