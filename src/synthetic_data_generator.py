import pandas as pd
import numpy as np

rows = 5000

data = {
    'ndvi': np.random.uniform(0.1, 0.9, rows),
    'soil_moisture': np.random.uniform(5, 60, rows),
    'temperature': np.random.uniform(15, 42, rows),
    'rainfall': np.random.uniform(0, 200, rows),
    'humidity': np.random.uniform(20, 95, rows),
    'wind_speed': np.random.uniform(0, 40, rows),
    'solar_radiation': np.random.uniform(100, 1000, rows),
    'irrigation_hours': np.random.uniform(0, 12, rows),
    'crop_type': np.random.choice(['soy', 'corn', 'cotton'], rows),
    'region': np.random.choice(['north', 'south', 'west'], rows)
}

df = pd.DataFrame(data)

conditions = [
    (df['soil_moisture'] < 15) & (df['temperature'] > 35),
    (df['soil_moisture'] < 25)
]

choices = [2, 1]

df['stress_risk'] = np.select(
    conditions,
    choices,
    default=0
)

df.to_csv(
    'data/synthetic/synthetic_agro_data.csv',
    index=False
)

print(df.head())