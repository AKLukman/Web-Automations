import requests
import pandas as pd

# Open-Meteo API endpoint
url = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude": 23.8103,       # Dhaka
    "longitude": 90.4125,
    "current_weather": True
}

response = requests.get(url, params=params)
data = response.json()

current = data["current_weather"]

weather = {
    "city": "Dhaka",
    "temperature_c": current["temperature"],
    "windspeed_kmh": current["windspeed"],
    "winddirection": current["winddirection"],
    "weathercode": current["weathercode"],
    "time": current["time"]
}

# Save using pandas

df = pd.DataFrame([weather])
df.to_csv("open_meteo_weather.csv", index=False)
print(weather)
print("Saved weather data to open_meteo_weather.csv")
