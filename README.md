# AI Pipeline for Agricultural Water Stress Prediction 🌱💧

## Visão Geral

O projeto **AI Pipeline for Agricultural Water Stress Prediction** tem como objetivo prever o risco de estresse hídrico em culturas agrícolas utilizando técnicas de Machine Learning e Explainable AI (XAI).

A solução combina:
- Engenharia de atributos;
- Pré-processamento automatizado;
- Modelos supervisionados de classificação;
- Interpretação de resultados com SHAP.

O pipeline foi desenvolvido para auxiliar produtores rurais, pesquisadores e profissionais do agronegócio na tomada de decisão relacionada ao manejo da irrigação e monitoramento agrícola.

---

# Contexto do Problema

O estresse hídrico é um dos principais fatores responsáveis pela redução da produtividade agrícola. A falta ou excesso de água afeta diretamente:
- Crescimento das plantas;
- Fotossíntese;
- Absorção de nutrientes;
- Qualidade da produção.

Monitorar esse fenômeno manualmente é custoso e pouco escalável. Com o avanço de sensores agrícolas e dados climáticos, tornou-se possível utilizar Inteligência Artificial para prever riscos de estresse hídrico com alta precisão.

Este projeto propõe um pipeline completo de IA capaz de:
- Processar dados ambientais e agrícolas;
- Identificar padrões associados ao estresse hídrico;
- Gerar previsões automatizadas;
- Explicar as decisões do modelo através de SHAP.

---

# Fonte dos Dados

Os dados utilizados no projeto são sintéticos e foram gerados para simular cenários agrícolas realistas.

## Variáveis Utilizadas

### Variáveis Numéricas
- `ndvi`
- `soil_moisture`
- `temperature`
- `rainfall`
- `humidity`
- `wind_speed`
- `solar_radiation`
- `irrigation_hours`

### Variáveis Categóricas
- `crop_type`
- `region`

### Variável Alvo
- `stress_risk`

---

# Metodologia Utilizada

O pipeline foi estruturado nas seguintes etapas:

## 1. Geração dos Dados
Criação de um dataset sintético contendo:
- Informações climáticas;
- Umidade do solo;
- Índices de vegetação;
- Tipo de cultura;
- Região agrícola.

---

## 2. Feature Engineering

Foram aplicadas técnicas de preparação e transformação dos dados:
- Separação entre variáveis numéricas e categóricas;
- Codificação One-Hot Encoding;
- Normalização de atributos numéricos;
- Construção de pipelines reutilizáveis.

---

## 3. Pré-processamento

Foi utilizado o `ColumnTransformer` do Scikit-Learn para:
- Padronizar atributos numéricos;
- Transformar variáveis categóricas;
- Garantir compatibilidade com os modelos.

---

## 4. Treinamento dos Modelos

Os modelos foram treinados utilizando pipelines completos integrados ao pré-processamento.

---

# Modelos Testados

## 🌲 Random Forest Classifier

Modelo baseado em múltiplas árvores de decisão.

### Vantagens
- Boa performance em dados tabulares;
- Redução de overfitting;
- Fácil interpretação de importância de atributos.

---

## ⚡ XGBoost Classifier

Modelo baseado em Gradient Boosting otimizado.

### Vantagens
- Alta capacidade preditiva;
- Excelente desempenho em problemas supervisionados;
- Melhor tratamento de padrões complexos.

---

# Resultados Obtidos

## Comparação dos Modelos

| Modelo | Accuracy | Precision | Recall | F1-Score | ROC-AUC |
|---|---|---|---|---|---|
| Random Forest | 0.998 | 0.998 | 0.998 | 0.998 | 1.000 |
| XGBoost | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

---

## Melhor Modelo

O modelo **XGBoost** apresentou o melhor desempenho geral, atingindo:
- 100% de Accuracy;
- 100% de Precision;
- 100% de Recall;
- ROC-AUC igual a 1.0.

---

# Interpretação com SHAP 🔍

Para garantir interpretabilidade do modelo, foi utilizada a biblioteca **SHAP (SHapley Additive exPlanations)**.

## Objetivos do SHAP
- Identificar quais variáveis mais impactam a previsão;
- Explicar decisões individuais;
- Aumentar transparência do modelo.

---

## Principais Features Identificadas

| Feature | Importância |
|---|---|
| soil_moisture | 3.53 |
| temperature | 0.89 |
| region_north | 0.04 |
| humidity | 0.03 |
| crop_type_cotton | 0.03 |

---

## Insights Obtidos

### Umidade do Solo (`soil_moisture`)
Foi a variável mais relevante do modelo.

Baixos níveis de umidade aumentam significativamente o risco de estresse hídrico.

---

### Temperatura (`temperature`)
Temperaturas elevadas estão fortemente associadas ao aumento do estresse nas plantações.

---

### Umidade Relativa (`humidity`)
Ambientes menos úmidos aumentam o risco de perda de água pelas plantas.

---

## Visualizações SHAP Geradas

O projeto inclui:
- SHAP Summary Plot;
- SHAP Bar Plot;
- Explicações individuais por amostra.

Essas visualizações permitem compreender:
- Impacto global das features;
- Impacto local em previsões específicas;
- Relação entre variáveis e classes previstas.

---

# Estrutura do Projeto

```bash
AI-Pipeline-Water-Stress/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── models/
│   ├── random_forest_model.pkl
│   └── xgboost_model.pkl
│
├── notebooks/
│   └── shap.ipynb
│
├── src/
│   ├── preprocessing.py
│   ├── training.py
│   └── explainability.py
│
├── requirements.txt
└── README.md
```

---

# Tecnologias Utilizadas

- Python
- Pandas
- NumPy
- Scikit-Learn
- XGBoost
- SHAP
- Matplotlib
- Seaborn
- Joblib

---

# Instruções para Execução do Projeto 🚀

## 1. Clone o Repositório

```bash
git clone https://github.com/seu-usuario/AI-Pipeline-Water-Stress.git
```

---

## 2. Acesse a Pasta

```bash
cd AI-Pipeline-Water-Stress
```

---

## 3. Crie um Ambiente Virtual

### Linux/Mac
```bash
python -m venv venv
source venv/bin/activate
```

### Windows
```bash
python -m venv venv
venv\Scripts\activate
```

---

## 4. Instale as Dependências

```bash
pip install -r requirements.txt
```

---

## 5. Execute o Notebook

```bash
jupyter notebook
```

Abra:
```bash
notebooks/shap.ipynb
```

---

# Link da Aplicação em Funcionamento 🌐

Substitua pelo link real da aplicação:

```text
https://seu-app-aqui.streamlit.app
```

---

# Possíveis Melhorias Futuras

- Integração com dados reais de sensores IoT;
- Uso de imagens de satélite;
- Deploy com Streamlit;
- Monitoramento em tempo real;
- API REST para inferência;
- Dashboard analítico.

---

# Conclusão

O projeto demonstra como técnicas modernas de Machine Learning e Explainable AI podem ser aplicadas no agronegócio para prever riscos de estresse hídrico com alta precisão.

Além do excelente desempenho preditivo, o uso de SHAP torna o modelo interpretável e mais confiável para aplicações reais no setor agrícola.

---

# Autor

Desenvolvido para fins acadêmicos e demonstrativos utilizando Inteligência Artificial aplicada ao Agronegócio.


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

