import joblib
import pandas as pd

model = joblib.load(
    'models/xgboost_model.pkl'
)

sample = pd.DataFrame({
    'ndvi': [0.35],
    'soil_moisture': [12],
    'temperature': [39],
    'rainfall': [5],
    'humidity': [25],
    'wind_speed': [20],
    'solar_radiation': [850],
    'irrigation_hours': [1],
    'crop_type': ['soy'],
    'region': ['north']
})

prediction = model.predict(sample)

print(f"Predicted Risk: {prediction[0]}")
