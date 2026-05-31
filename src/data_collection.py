import requests
import pandas as pd

API_KEY = "04608083745e79e0774c0fd383f208ec"

url = f"https://api.openweathermap.org/data/2.5/weather?q=SaoPaulo&appid={API_KEY}"


response = requests.get(url)

data = response.json()
print(data)

weather = {
    "temperature": data["main"]["temp"],
    "humidity": data["main"]["humidity"],
    "wind_speed": data["wind"]["speed"]
}

df = pd.DataFrame([weather])

df.to_csv(
    "weather_data.csv",
    index=False
)

print(df)