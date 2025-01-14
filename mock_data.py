# 模拟天气数据
WEATHER_DATA = {
    "北京": {
        "temperature": "36°C",
        "weather": "高温",
        "precipitation_probability": "10%",
        "wind_speed": "15km/h"
    },
    "上海": {
        "temperature": "30°C",
        "weather": "阵雨",
        "precipitation_probability": "70%",
        "wind_speed": "20km/h"
    },
    "广州": {
        "temperature": "32°C",
        "weather": "大雨",
        "precipitation_probability": "90%",
        "wind_speed": "25km/h"
    }
}

EXTREME_WEATHER_DATA = {
    "北京": {
        "extreme_weather": "高温预警",
        "level": "橙色",
        "suggestion": "避免中午外出，补充水分"
    },
    "上海": {
        "extreme_weather": "暴雨预警",
        "level": "黄色",
        "suggestion": "注意防范积水"
    },
    "广州": {
        "extreme_weather": "台风预警",
        "level": "红色",
        "suggestion": "避免外出，关好门窗"
    }
}

AIR_QUALITY_DATA = {
    "北京": {
        "aqi": "120",
        "level": "轻度污染",
        "suggestion": "外出佩戴口罩"
    },
    "上海": {
        "aqi": "80",
        "level": "良好",
        "suggestion": "正常活动"
    },
    "广州": {
        "aqi": "150",
        "level": "中度污染",
        "suggestion": "减少户外活动"
    }
}

WEATHER_HISTORY_DATA = {
    "北京": {
        "average_high": "33°C",
        "abnormal_days": "5天"
    },
    "上海": {
        "average_high": "31°C",
        "abnormal_days": "3天"
    },
    "广州": {
        "average_high": "35°C",
        "abnormal_days": "7天"
    }
}

TYPHOON_PATH_DATA = {
    "latest": {
        "typhoon_location": "广东沿海",
        "moving_direction": "北偏东",
        "affected_area": "华南、华东"
    }
}

CITY_RISK_DATA = {
    "北京": {
        "risk_level": "低",
        "suggestion": "注意降水可能"
    },
    "上海": {
        "risk_level": "中",
        "suggestion": "做好防洪准备"
    },
    "广州": {
        "risk_level": "高",
        "suggestion": "避免外出，储备物资"
    }
}

TRAFFIC_STATUS_DATA = {
    "北京": {
        "traffic_condition": "畅通"
    },
    "上海": {
        "traffic_condition": "拥堵"
    },
    "广州": {
        "traffic_condition": "严重拥堵"
    }
}
