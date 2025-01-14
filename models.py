from pydantic import BaseModel
from typing import Optional, List

class WeatherData(BaseModel):
    temperature: str
    weather: str
    precipitation_probability: str
    wind_speed: Optional[str] = None

class ExtremeWeather(BaseModel):
    extreme_weather: str
    level: str
    suggestion: str

class AirQuality(BaseModel):
    aqi: str
    level: str
    suggestion: str

class WeatherHistory(BaseModel):
    average_high: str
    abnormal_days: str

class TyphoonPath(BaseModel):
    typhoon_location: str
    moving_direction: str
    affected_area: str

class CityRisk(BaseModel):
    risk_level: str
    suggestion: str

class TrafficStatus(BaseModel):
    traffic_condition: str
