# AI Pipeline for Agricultural Water Stress Prediction 🌱💧

## Sobre o Projeto

O projeto **AI Pipeline for Agricultural Water Stress Prediction** é uma demonstração técnica de um dos módulos da **Space Intelligence Platform**, uma infraestrutura de inteligência espacial aplicada ao monitoramento e tomada de decisão no mundo físico.

Este repositório representa um recorte específico focado em:
- Predição de estresse hídrico agrícola;
- Modelos preditivos baseados em Machine Learning;
- Explainable AI com SHAP;
- Processamento de dados ambientais simulados.

Enquanto este projeto demonstra um pipeline isolado de IA para agricultura, a visão da plataforma maior é integrar:
- Dados satelitais;
- Sensores IoT;
- Inteligência geoespacial;
- Dados climáticos;
- Sistemas operacionais corporativos;
- IA multimodal;
- Infraestrutura distribuída Edge + Cloud + Orbital.

---

# Space Intelligence Platform 🚀🌍

A **Space Intelligence Platform** é uma infraestrutura tecnológica de próxima geração que conecta:
- Satélites;
- Sensores terrestres;
- Redes de conectividade híbrida;
- Inteligência Artificial multimodal;
- Sistemas operacionais empresariais.

Seu objetivo é transformar bilhões de sinais físicos em inteligência operacional acionável em tempo real.

A plataforma funciona como um:
> “Sistema Operacional Inteligente do Mundo Físico”.

---

## Visão da Plataforma

A arquitetura principal é dividida em quatro camadas:

### 1. Orbital Layer
Responsável pela aquisição de dados espaciais:
- Satélites ópticos;
- Satélites SAR;
- Dados meteorológicos;
- Sensores hiperespectrais;
- Redes GNSS e LEO.

---

### 2. Ground Layer
Integra dispositivos físicos conectados:
- Sensores IoT;
- Estações meteorológicas;
- Máquinas agrícolas;
- Drones;
- Redes LoRaWAN;
- Infraestrutura Edge Computing.

---

### 3. Intelligence Layer
Camada cognitiva baseada em IA multimodal:
- Computer Vision;
- Forecasting;
- Graph AI;
- LLMs especializados;
- Reinforcement Learning.

---

### 4. Action Layer
Camada operacional responsável por:
- Dashboards geoespaciais;
- Alertas inteligentes;
- APIs corporativas;
- Automação operacional;
- Integração com ERPs e sistemas externos.

---

# Relação deste Projeto com a Plataforma

O módulo de **Agricultural Water Stress Prediction** representa um exemplo prático de aplicação da camada de inteligência da plataforma.

Ele simula como dados ambientais podem ser processados para:
- Detectar riscos agrícolas;
- Antecipar perdas;
- Gerar inteligência preditiva;
- Auxiliar operações agrícolas em larga escala.

Este pipeline pode futuramente ser integrado a:
- Dados satelitais reais;
- Sensores agrícolas em tempo real;
- APIs meteorológicas;
- Infraestrutura geoespacial distribuída.

---

# Visão Geral do Pipeline

O projeto tem como objetivo prever o risco de estresse hídrico em culturas agrícolas utilizando técnicas de:
- Machine Learning;
- Engenharia de atributos;
- Pré-processamento automatizado;
- Explainable AI (XAI).

A solução foi desenvolvida para demonstrar como inteligência artificial pode apoiar:
- Agricultura de precisão;
- Monitoramento ambiental;
- Gestão hídrica;
- Decisões operacionais agrícolas.

---

# Contexto do Problema

O estresse hídrico é um dos principais fatores responsáveis pela redução da produtividade agrícola.

A falta ou excesso de água impacta diretamente:
- Crescimento vegetal;
- Fotossíntese;
- Absorção de nutrientes;
- Qualidade da produção.

Monitorar esse fenômeno manualmente é caro, pouco escalável e altamente dependente de análises humanas.

Com o avanço de:
- Sensores IoT;
- Satélites;
- Dados climáticos;
- Inteligência Artificial;

tornou-se possível criar modelos preditivos capazes de antecipar riscos agrícolas com alta precisão.

---

# Fonte dos Dados

Os dados utilizados neste projeto são sintéticos e foram gerados para simular cenários agrícolas realistas.

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
- One-Hot Encoding;
- Normalização de atributos;
- Construção de pipelines reutilizáveis.

---

## 3. Pré-processamento

Foi utilizado o `ColumnTransformer` do Scikit-Learn para:
- Padronização numérica;
- Transformação categórica;
- Integração com os modelos.

---

## 4. Treinamento dos Modelos

Os modelos foram treinados utilizando pipelines completos integrados ao pré-processamento.

---

# Modelos Testados

## 🌲 Random Forest Classifier

### Vantagens
- Robustez;
- Boa generalização;
- Interpretação simples.

---

## ⚡ XGBoost Classifier

### Vantagens
- Alto desempenho;
- Excelente capacidade preditiva;
- Eficiência em dados tabulares.

---

# Resultados Obtidos

| Modelo | Accuracy | Precision | Recall | F1-Score | ROC-AUC |
|---|---|---|---|---|---|
| Random Forest | 0.998 | 0.998 | 0.998 | 0.998 | 1.000 |
| XGBoost | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

---

# Melhor Modelo

O modelo **XGBoost** apresentou o melhor desempenho geral:
- Accuracy: 100%;
- Precision: 100%;
- Recall: 100%;
- ROC-AUC: 1.0.

---

# Interpretação com SHAP 🔍

Foi utilizada a biblioteca **SHAP (SHapley Additive exPlanations)** para aumentar a interpretabilidade do modelo.

## Objetivos do SHAP
- Explicar previsões;
- Identificar variáveis relevantes;
- Aumentar transparência do pipeline.

---

## Features Mais Importantes

| Feature | Importância |
|---|---|
| soil_moisture | 3.53 |
| temperature | 0.89 |
| region_north | 0.04 |
| humidity | 0.03 |
| crop_type_cotton | 0.03 |

---

## Insights Obtidos

### Soil Moisture
Baixos níveis de umidade do solo aumentam significativamente o risco de estresse hídrico.

### Temperature
Temperaturas elevadas contribuem para aumento do estresse nas culturas.

### Humidity
Ambientes secos aumentam a perda de água das plantas.

---

# Tecnologias Utilizadas

- Python
- Pandas
- NumPy
- Scikit-Learn
- XGBoost
- SHAP
- Matplotlib
- Joblib

---
# Como Utilar a Aplicação 🚀

A aplicação foi desenvolvida com **Streamlit** e permite simular cenários agrícolas para prever o nível de risco de estresse hídrico utilizando Inteligência Artificial.

O usuário pode ajustar variáveis ambientais e agrícolas diretamente pela interface para obter previsões em tempo real.

## Link da Aplicação 🌐

```text
https://space-intelligence-platform-ai.onrender.com/
```

## Interface da Aplicação

Ao abrir a aplicação, serão exibidos campos interativos para preenchimento dos dados agrícolas.

## Variáveis Disponíveis

### 🌿 NDVI

Índice de vegetação utilizado para medir a saúde da plantação.

Faixa:

```text
0.0 → 1.0
```

* Valores maiores indicam vegetação mais saudável;
* Valores menores podem indicar degradação ou estresse.

---

### 💧 Soil Moisture

Representa a umidade do solo.

Faixa:

```text
0 → 100
```

* Valores baixos aumentam o risco de estresse hídrico;
* Valores altos indicam maior disponibilidade de água.

---

### 🌡️ Temperature

Temperatura ambiente em graus Celsius.

Faixa:

```text
0 → 50
```

Temperaturas elevadas podem aumentar o risco de perda hídrica nas culturas.

---

### 🌧️ Rainfall

Quantidade de chuva acumulada.

Faixa:

```text
0 → 300
```

Baixos níveis de precipitação podem impactar diretamente o estresse das plantações.

---

### 💨 Humidity

Umidade relativa do ar.

Faixa:

```text
0 → 100
```

Ambientes muito secos aumentam a evapotranspiração das plantas.

---

### 🌱 Crop Type

Tipo de cultura agrícola analisada.

Opções disponíveis:

* Soy
* Corn
* Cotton

---

### 🌍 Region

Região agrícola simulada.

Opções disponíveis:

* North
* South
* West

---

## Como Fazer uma Predição

### 1. Ajuste os parâmetros

Utilize os sliders e caixas de seleção para configurar o cenário agrícola desejado.

---

### 2. Aguarde a inferência do modelo

A aplicação envia automaticamente os dados para o modelo treinado em XGBoost.

---

### 3. Visualize o resultado

A IA retornará uma das seguintes classificações:

| Resultado   | Significado                     |
| ----------- | ------------------------------- |
| Low Risk    | Baixo risco de estresse hídrico |
| Medium Risk | Risco moderado                  |
| High Risk   | Alto risco de estresse hídrico  |

---

# Objetivo da Demonstração

Esta aplicação representa uma demonstração simplificada de um dos módulos da **Space Intelligence Platform**, mostrando como:

* IA preditiva;
* Dados ambientais;
* Modelos de Machine Learning;
* Inteligência operacional;

podem ser utilizados para antecipar riscos agrícolas em tempo real.

---

# Conclusão

Este projeto demonstra como técnicas modernas de:
- Machine Learning;
- Explainable AI;
- Processamento geoespacial;
- Inteligência operacional;

podem ser aplicadas para prever riscos agrícolas e apoiar decisões estratégicas.

Além disso, o pipeline representa um exemplo prático de como módulos inteligentes podem compor infraestruturas maiores como a **Space Intelligence Platform**, conectando dados espaciais, sensores físicos e IA em uma arquitetura operacional integrada.

---

# Autores

Projeto desenvolvido para fins acadêmicos, demonstrativos e de pesquisa aplicada em:
- Inteligência Artificial;
- Geospatial AI;
- Agricultura de Precisão;
- Space Intelligence Systems.
