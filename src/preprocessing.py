import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

df = pd.read_csv(
    'data/processed/final_dataset.csv'
)

X = df.drop('stress_risk', axis=1)
y = df['stress_risk']

numeric_features = [
    'ndvi',
    'soil_moisture',
    'temperature',
    'rainfall',
    'humidity',
    'wind_speed',
    'solar_radiation',
    'irrigation_hours'
]

categorical_features = [
    'crop_type',
    'region'
]

preprocessor = ColumnTransformer(
    transformers=[
        (
            'num',
            StandardScaler(),
            numeric_features
        ),
        (
            'cat',
            OneHotEncoder(),
            categorical_features
        )
    ]
)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)