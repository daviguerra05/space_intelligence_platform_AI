# Space Intelligence Platform

## AI Pipeline for Agricultural Water Stress Prediction

### Run locally

```bash
pip install -r requirements.txt


space-intelligence-ml/
│
├── data/
│   ├── raw/
│   │   ├── satellite_data.csv
│   │   ├── weather_data.csv
│   │   └── iot_sensor_data.csv
│   │
│   ├── processed/
│   │   └── final_dataset.csv
│   │
│   └── synthetic/
│       └── synthetic_agro_data.csv
│
├── src/
│   ├── data_collection.py
│   ├── synthetic_data_generator.py
│   ├── preprocessing.py
│   ├── feature_engineering.py
│   ├── train_random_forest.py
│   ├── train_xgboost.py
│   ├── evaluate_models.py
│   ├── shap_analysis.py
│   ├── predict.py
│   └── app.py
│
├── models/
│   ├── random_forest.pkl
│   └── xgboost_model.pkl
│
├── outputs/
│   ├── figures/
│   │   ├── confusion_matrix.png
│   │   ├── feature_importance.png
│   │   └── shap_summary.png
│   │
│   └── reports/
│       └── metrics_report.txt
│
├── requirements.txt
├── Dockerfile
├── README.md
└── .gitignore


Bash
streamlit run src/app.py

