import streamlit as st
import pandas as pd
import joblib

model = joblib.load(
    '../models/xgboost_model.pkl'
)

st.title("Space Intelligence Platform")

ndvi = st.slider('NDVI', 0.0, 1.0)
soil = st.slider('Soil Moisture', 0, 100)
temp = st.slider('Temperature', 0, 50)
rain = st.slider('Rainfall', 0, 300)
humidity = st.slider('Humidity', 0, 100)

crop = st.selectbox(
    'Crop Type',
    ['soy', 'corn', 'cotton']
)

region = st.selectbox(
    'Region',
    ['north', 'south', 'west']
)

input_data = pd.DataFrame({
    'ndvi': [ndvi],
    'soil_moisture': [soil],
    'temperature': [temp],
    'rainfall': [rain],
    'humidity': [humidity],
    'wind_speed': [15],
    'solar_radiation': [700],
    'irrigation_hours': [4],
    'crop_type': [crop],
    'region': [region]
})

prediction = model.predict(input_data)

risk_map = {
    0: 'Low Risk',
    1: 'Medium Risk',
    2: 'High Risk'
}

st.subheader(
    f"Prediction: {risk_map[prediction[0]]}"
)