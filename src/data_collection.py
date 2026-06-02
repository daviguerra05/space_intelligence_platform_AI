import requests
import pandas as pd
import os

teste = "04608083745e79e0774c0fd383f208ec"

API_KEY = os.getenv("API_KEY")

# url = f"https://api.openweathermap.org/data/2.5/weather?q=SaoPaulo&appid={API_KEY}"

lat = -23.501534335458278
lon = -46.664206855471015

url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}"

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
    "data/raw/weather_data.csv",
    index=False
)

print(df)