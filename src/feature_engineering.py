import pandas as pd

df = pd.read_csv(
    'synthetic_agro_data.csv'
)

df['climate_index'] = (
    df['temperature'] * 0.4 +
    df['humidity'] * 0.2 -
    df['rainfall'] * 0.3
)

df['water_balance'] = (
    df['rainfall'] +
    df['irrigation_hours'] * 10 -
    df['temperature']
)

df.to_csv(
    'final_dataset.csv',
    index=False
)