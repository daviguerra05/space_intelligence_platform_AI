import joblib
import pandas as pd

from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier

from preprocessing import (
    X_train,
    y_train,
    preprocessor
)

rf_pipeline = Pipeline([
    ('preprocessor', preprocessor),
    (
        'classifier',
        RandomForestClassifier(
            n_estimators=200,
            max_depth=10,
            random_state=42
        )
    )
])

rf_pipeline.fit(X_train, y_train)

joblib.dump(
    rf_pipeline,
    'models/random_forest.pkl'
)

print("Random Forest trained.")