from fastapi import FastAPI, HTTPException
from models import *
from mock_data import *

app = FastAPI(
    title="天气预报与灾害预警系统API",
    description="提供天气、空气质量、极端天气预警等相关数据的API服务",
    version="1.0.0"
)

@app.get("/")
async def root():
    return {"message": "欢迎使用天气预报与灾害预警系统API"}

@app.get("/weather/{city}", response_model=WeatherData)
async def get_weather(city: str):
    if city not in WEATHER_DATA:
        raise HTTPException(status_code=404, detail="城市未找到")
    return WEATHER_DATA[city]

@app.get("/extreme-weather/{city}", response_model=ExtremeWeather)
async def check_extreme_weather(city: str):
    if city not in EXTREME_WEATHER_DATA:
        raise HTTPException(status_code=404, detail="城市未找到")
    return EXTREME_WEATHER_DATA[city]

@app.get("/air-quality/{city}", response_model=AirQuality)
async def get_air_quality(city: str):
    if city not in AIR_QUALITY_DATA:
        raise HTTPException(status_code=404, detail="城市未找到")
    return AIR_QUALITY_DATA[city]

@app.get("/weather-history/{city}", response_model=WeatherHistory)
async def analyze_weather_history(city: str):
    if city not in WEATHER_HISTORY_DATA:
        raise HTTPException(status_code=404, detail="城市未找到")
    return WEATHER_HISTORY_DATA[city]

@app.get("/typhoon-path/{typhoon_id}", response_model=TyphoonPath)
async def get_typhoon_path(typhoon_id: str):
    if typhoon_id not in TYPHOON_PATH_DATA:
        raise HTTPException(status_code=404, detail="台风数据未找到")
    return TYPHOON_PATH_DATA[typhoon_id]

@app.get("/city-risk/{city}", response_model=CityRisk)
async def assess_city_risk(city: str):
    if city not in CITY_RISK_DATA:
        raise HTTPException(status_code=404, detail="城市未找到")
    return CITY_RISK_DATA[city]

@app.get("/traffic-status/{city}", response_model=dict)
async def get_traffic_status(city: str):
    if city not in TRAFFIC_STATUS_DATA:
        raise HTTPException(status_code=404, detail="城市未找到")
    return TRAFFIC_STATUS_DATA[city]
