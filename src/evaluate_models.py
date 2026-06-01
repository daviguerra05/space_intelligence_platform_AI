import joblib

from sklearn.metrics import (
    classification_report,
    confusion_matrix
)

from preprocessing import (
    X_test,
    y_test
)

rf_model = joblib.load(
    'random_forest.pkl'
)

xgb_model = joblib.load(
    'xgboost_model.pkl'
)

rf_predictions = rf_model.predict(X_test)
xgb_predictions = xgb_model.predict(X_test)

print("Random Forest")
print(classification_report(
    y_test,
    rf_predictions
))

print("XGBoost")
print(classification_report(
    y_test,
    xgb_predictions
))