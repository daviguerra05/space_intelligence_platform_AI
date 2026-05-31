import joblib

from sklearn.pipeline import Pipeline
from xgboost import XGBClassifier

from preprocessing import (
    X_train,
    y_train,
    preprocessor
)

xgb_pipeline = Pipeline([
    ('preprocessor', preprocessor),
    (
        'classifier',
        XGBClassifier(
            n_estimators=300,
            learning_rate=0.05,
            max_depth=8
        )
    )
])

xgb_pipeline.fit(X_train, y_train)

joblib.dump(
    xgb_pipeline,
    '../models/xgboost_model.pkl'
)

print("XGBoost trained.")