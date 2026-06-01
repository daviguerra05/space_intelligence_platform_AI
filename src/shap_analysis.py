import joblib
import shap

from preprocessing import X_test

model = joblib.load(
    'xgboost_model.pkl'
)

classifier = model.named_steps['classifier']
preprocessor = model.named_steps['preprocessor']

X_processed = preprocessor.transform(X_test)

explainer = shap.TreeExplainer(classifier)

shap_values = explainer.shap_values(X_processed)

shap.summary_plot(
    shap_values,
    X_processed
)