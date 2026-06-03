# AI Pipeline para Predição de Estresse Hídrico Agrícola 🌱💧

## Visão Geral do Projeto

Este projeto demonstra um pipeline de Inteligência Artificial focado na **predição de estresse hídrico em culturas agrícolas**, utilizando Machine Learning e Explainable AI (XAI). Ele serve como uma prova de conceito para um dos módulos da **Space Intelligence Platform**, uma infraestrutura tecnológica inovadora para monitoramento e tomada de decisão no mundo físico.

Neste repositório, você encontrará:
*   Modelos preditivos de Machine Learning (Random Forest, XGBoost)
*   Análise de interpretabilidade com SHAP
*   Processamento de dados ambientais simulados
*   Uma aplicação interativa para simulação de cenários

## Space Intelligence Platform 🚀🌍

A **Space Intelligence Platform** é uma infraestrutura tecnológica de próxima geração que integra dados de satélites, sensores terrestres, conectividade híbrida, Inteligência Artificial multimodal e sistemas operacionais empresariais. Seu objetivo é transformar bilhões de sinais físicos em inteligência operacional acionável em tempo real, funcionando como um "Sistema Operacional Inteligente do Mundo Físico".

### Arquitetura da Plataforma

A plataforma é composta por quatro camadas interconectadas:

1.  **Orbital Layer**: Aquisição de dados espaciais (satélites ópticos/SAR, dados meteorológicos, sensores hiperespectrais, redes GNSS/LEO).
2.  **Ground Layer**: Integração de dispositivos físicos (sensores IoT, estações meteorológicas, máquinas agrícolas, drones, redes LoRaWAN, Edge Computing).
3.  **Intelligence Layer**: Camada cognitiva baseada em IA multimodal (Computer Vision, Forecasting, Graph AI, LLMs especializados, Reinforcement Learning).
4.  **Action Layer**: Camada operacional para dashboards geoespaciais, alertas inteligentes, APIs corporativas e automação operacional.

### Relação com Este Projeto

O módulo de **Agricultural Water Stress Prediction** é um exemplo prático da **Intelligence Layer**. Ele simula o processamento de dados ambientais para detectar riscos agrícolas, antecipar perdas e gerar inteligência preditiva, que pode futuramente ser integrada a dados reais de satélites e sensores.

## Contexto do Problema: Estresse Hídrico na Agricultura

O estresse hídrico é um fator crítico na redução da produtividade agrícola. Monitorar esse fenômeno manualmente é ineficiente. Com o avanço de sensores, satélites e IA, é possível criar modelos preditivos para antecipar esses riscos com alta precisão, apoiando a agricultura de precisão, gestão hídrica e decisões operacionais.

## Como Utilizar a Aplicação 🚀

Experimente a aplicação interativa desenvolvida com **Streamlit** para simular cenários agrícolas e prever o risco de estresse hídrico.

**Link da Aplicação**: [https://space-intelligence-platform-ai.onrender.com/](https://space-intelligence-platform-ai.onrender.com/)

**Observação**: A aplicação está hospedada no plano gratuito do Render. O primeiro acesso pode demorar alguns segundos para inicializar o servidor.

### Interface e Variáveis Disponíveis

A interface permite ajustar variáveis ambientais e agrícolas para obter previsões em tempo real:

*   **🌿 NDVI (0.0 - 1.0)**: Índice de vegetação (saúde da plantação).
*   **💧 Soil Moisture (0 - 100)**: Umidade do solo.
*   **🌡️ Temperature (0 - 50 °C)**: Temperatura ambiente.
*   **🌧️ Rainfall (0 - 300 mm)**: Quantidade de chuva acumulada.
*   **💨 Humidity (0 - 100 %)**: Umidade relativa do ar.
*   **🌱 Crop Type**: Tipo de cultura (Soy, Corn, Cotton).
*   **🌍 Region**: Região agrícola simulada (North, South, West).

### Fazendo uma Predição

1.  **Ajuste os parâmetros**: Use os controles da interface para definir o cenário.
2.  **Aguarde a inferência do modelo**: A aplicação envia os dados ao modelo XGBoost.
3.  **Visualize o resultado**: A IA classifica o risco como:
    *   **Low Risk**: Baixo risco de estresse hídrico
    *   **Medium Risk**: Risco moderado
    *   **High Risk**: Alto risco de estresse hídrico

## Metodologia e Modelos

O pipeline envolve:
1.  **Geração dos Dados**: Dataset sintético de informações climáticas, umidade do solo, índices de vegetação, tipo de cultura e região.
2.  **Feature Engineering & Pré-processamento**: Separação de variáveis, One-Hot Encoding, normalização e uso de `ColumnTransformer` do Scikit-Learn.
3.  **Treinamento dos Modelos**: Pipelines completos com Random Forest e XGBoost.

### Modelos Testados e Resultados

| Modelo          | Accuracy | Precision | Recall | F1-Score | ROC-AUC |
|-----------------|----------|-----------|--------|----------|---------|
| Random Forest   | 0.998    | 0.998     | 0.998  | 0.998    | 1.000   |
| XGBoost         | 1.000    | 1.000     | 1.000  | 1.000    | 1.000   |

O modelo **XGBoost** demonstrou o melhor desempenho geral, com todas as métricas em 100%.

### Interpretação com SHAP 🔍

A biblioteca **SHAP (SHapley Additive exPlanations)** foi utilizada para explicar as previsões do modelo e identificar as variáveis mais importantes:

| Feature         | Importância |
|-----------------|-------------|
| soil_moisture   | 3.53        |
| temperature     | 0.89        |
| region_north    | 0.04        |
| humidity        | 0.03        |
| crop_type_cotton| 0.03        |

**Insights Principais**:
*   **Soil Moisture**: Baixos níveis de umidade aumentam significativamente o risco.
*   **Temperature**: Temperaturas elevadas contribuem para o estresse.
*   **Humidity**: Ambientes secos aumentam a perda de água das plantas.

## Tecnologias Utilizadas

*   Python
*   Pandas
*   NumPy
*   Scikit-Learn
*   XGBoost
*   SHAP
*   Matplotlib
*   Joblib
*   Streamlit

## Conclusão

Este projeto demonstra a aplicação de Machine Learning e Explainable AI para prever riscos agrícolas, servindo como um componente inteligente para infraestruturas maiores como a **Space Intelligence Platform**. Ele evidencia o potencial da IA para conectar dados espaciais e sensores físicos, otimizando decisões estratégicas na agricultura.

## Autores

*   Davi Passanha de Sousa Guerra - RM551605
*   Cauã Gonçalves de Jesus - RM97648
*   Luan Silveira Macea - RM98290
*   Rui Amorim Siqueira - RM98436
*   Luigi Ferrara Sinno - RM98047
