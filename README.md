# AI Pipeline para Predição de Estresse Hídrico Agrícola 🌱💧

## Sobre o Projeto

O projeto **AI Pipeline para Predição de Estresse Hídrico Agrícola** é uma demonstração técnica aprofundada de um dos módulos da **Space Intelligence Platform**, uma infraestrutura de inteligência espacial projetada para o monitoramento e tomada de decisão em cenários do mundo físico. Este repositório oferece uma visão detalhada de como a Inteligência Artificial pode ser aplicada para resolver problemas críticos na agricultura moderna.

Este recorte específico do pipeline foca em:
*   **Predição de Estresse Hídrico Agrícola**: Utilização de modelos avançados para identificar e prever condições de estresse hídrico em culturas.
*   **Modelos Preditivos Baseados em Machine Learning**: Implementação e comparação de algoritmos de Machine Learning para máxima precisão e robustez.
*   **Explainable AI (XAI) com SHAP**: Garantia de transparência e interpretabilidade dos modelos, crucial para a confiança e adoção em campo.
*   **Processamento de Dados Ambientais Simulados**: Demonstração de todo o ciclo de vida dos dados, desde a geração até a inferência, utilizando dados sintéticos que mimetizam cenários reais.

Embora este projeto demonstre um pipeline de IA isolado para a agricultura, a visão da plataforma maior é integrar de forma holística:
*   Dados satelitais
*   Sensores IoT (Internet das Coisas)
*   Inteligência geoespacial
*   Dados climáticos
*   Sistemas operacionais corporativos (ERPs, CRMs)
*   IA multimodal (visão computacional, processamento de linguagem natural, etc.)
*   Infraestrutura distribuída Edge + Cloud + Orbital

---

# Space Intelligence Platform 🚀🌍

A **Space Intelligence Platform** é uma infraestrutura tecnológica de próxima geração, projetada para conectar um ecossistema complexo de componentes:
*   **Satélites**: Fontes de dados remotos de larga escala.
*   **Sensores terrestres**: Coleta de dados em tempo real e de alta granularidade.
*   **Redes de conectividade híbrida**: Garantia de comunicação eficiente em diferentes ambientes.
*   **Inteligência Artificial multimodal**: Capacidade de processar e correlacionar diversos tipos de dados.
*   **Sistemas operacionais empresariais**: Integração com processos de negócio e automação de fluxos de trabalho.

Seu objetivo primordial é transformar bilhões de sinais físicos, coletados de diversas fontes, em inteligência operacional acionável em tempo real, permitindo decisões proativas e otimizadas. A plataforma funciona como um:

> “Sistema Operacional Inteligente do Mundo Físico”.

---

## Visão da Arquitetura da Plataforma

A arquitetura principal da Space Intelligence Platform é estratificada em quatro camadas distintas, cada uma com responsabilidades bem definidas:

### 1. Orbital Layer
Esta camada é responsável pela aquisição e coleta de dados espaciais em larga escala, provenientes de diversas fontes orbitais:
*   Satélites ópticos: Imagens visíveis e multiespectrais.
*   Satélites SAR (Radar de Abertura Sintética): Dados de radar para monitoramento independente das condições climáticas.
*   Dados meteorológicos: Informações climáticas globais e regionais.
*   Sensores hiperespectrais: Detalhamento espectral para análise avançada de materiais e condições.
*   Redes GNSS (Sistema Global de Navegação por Satélite) e LEO (Órbita Terrestre Baixa): Posicionamento preciso e comunicação de dados.

---

### 2. Ground Layer
A camada terrestre integra uma vasta gama de dispositivos físicos conectados e infraestruturas locais:
*   Sensores IoT: Coleta de dados ambientais, de solo e de cultura em tempo real.
*   Estações meteorológicas: Dados climáticos locais e precisos.
*   Máquinas agrícolas: Informações sobre operações e desempenho de equipamentos.
*   Drones: Mapeamento aéreo de alta resolução e inspeções localizadas.
*   Redes LoRaWAN: Conectividade de baixo consumo e longo alcance para dispositivos IoT.
*   Infraestrutura Edge Computing: Processamento de dados próximo à fonte para latência reduzida e maior eficiência.

---

### 3. Intelligence Layer
A camada de inteligência é o coração cognitivo da plataforma, baseada em IA multimodal para processar, analisar e gerar insights:
*   Computer Vision: Análise de imagens e vídeos (satélites, drones) para detecção de anomalias, contagem e classificação.
*   Forecasting: Modelos preditivos para antecipar tendências e eventos futuros.
*   Graph AI: Análise de relações complexas entre entidades e eventos.
*   LLMs especializados: Processamento de linguagem natural para extrair informações de relatórios, documentos e comunicação.
*   Reinforcement Learning: Otimização de decisões e automação de processos complexos.

---

### 4. Action Layer
Esta camada operacional é responsável por traduzir a inteligência gerada em ações concretas e interfaces amigáveis:
*   Dashboards geoespaciais: Visualizações interativas e intuitivas de dados espaciais e operacionais.
*   Alertas inteligentes: Notificações proativas sobre riscos, anomalias ou oportunidades.
*   APIs corporativas: Interface para integração com sistemas externos e desenvolvimento de novas aplicações.
*   Automação operacional: Disparo de ações automatizadas com base nos insights gerados.
*   Integração com ERPs e sistemas externos: Sincronização e fluxo de dados com sistemas de gestão empresarial.

---

# Relação Deste Projeto com a Plataforma

O módulo de **Agricultural Water Stress Prediction** representa um exemplo prático e tangível da aplicação da **Intelligence Layer** dentro da Space Intelligence Platform. Ele demonstra como um componente de IA específico pode ser desenvolvido e integrado para resolver um desafio complexo.

Este projeto simula como dados ambientais podem ser processados e analisados para:
*   **Detectar riscos agrícolas**: Identificar precocemente a probabilidade de estresse hídrico.
*   **Antecipar perdas**: Prever o impacto potencial na produtividade e qualidade da colheita.
*   **Gerar inteligência preditiva**: Fornecer informações valiosas para planejamento e gestão.
*   **Auxiliar operações agrícolas em larga escala**: Otimizar o uso de recursos como água e fertilizantes.

Este pipeline, embora demonstrativo, foi projetado com a modularidade em mente, podendo futuramente ser integrado com:
*   Dados satelitais reais (NDVI, índices de umidade de satélites)
*   Sensores agrícolas em tempo real (umidade do solo, temperatura, etc.)
*   APIs meteorológicas (previsão do tempo, histórico climático)
*   Infraestrutura geoespacial distribuída (para processamento e armazenamento eficiente de dados em grande volume)

---

# Visão Geral do Pipeline de IA

O projeto tem como objetivo principal prever o risco de estresse hídrico em culturas agrícolas. Para atingir este objetivo, o pipeline integra diversas técnicas de Machine Learning, engenharia de atributos, pré-processamento automatizado e Explainable AI (XAI). A solução foi desenvolvida para demonstrar como a inteligência artificial pode atuar como um pilar fundamental no apoio à:
*   Agricultura de precisão: Otimizando o manejo de culturas e recursos.
*   Monitoramento ambiental: Fornecendo insights sobre as condições do ecossistema agrícola.
*   Gestão hídrica: Facilitando decisões sobre irrigação e uso eficiente da água.
*   Decisões operacionais agrícolas: Oferecendo suporte baseado em dados para o dia a dia no campo.

---

# Contexto do Problema: Estresse Hídrico na Agricultura

O estresse hídrico é reconhecidamente um dos principais fatores abióticos responsáveis pela redução significativa da produtividade agrícola em diversas regiões do mundo. A gestão inadequada da água, seja por escassez ou excesso, impacta diretamente uma série de processos fisiológicos e de desenvolvimento das plantas:
*   Crescimento vegetal
*   Fotossíntese
*   Absorção de nutrientes
*   Qualidade da produção

Tradicionalmente, o monitoramento desse fenômeno é realizado manualmente, um processo que é inerentemente caro, pouco escalável e altamente dependente de análises humanas subjetivas e demoradas. No entanto, com o avanço tecnológico em diversas frentes, o cenário se transformou:
*   **Sensores IoT**: Disponibilidade de dados em tempo real e de alta granularidade sobre condições de solo e clima.
*   **Satélites**: Coleta contínua de dados de sensoriamento remoto em larga escala.
*   **Dados climáticos**: Modelos e previsões cada vez mais precisos.
*   **Inteligência Artificial**: Capacidade de processar grandes volumes de dados e identificar padrões complexos.

A convergência dessas tecnologias tornou possível a criação de modelos preditivos robustos e capazes de antecipar riscos agrícolas com alta precisão, permitindo uma intervenção mais oportuna e eficaz.

---

# Fonte dos Dados

Os dados utilizados neste projeto são sintéticos e foram cuidadosamente gerados para simular cenários agrícolas realistas. Essa abordagem permite o desenvolvimento e teste do pipeline de IA de forma controlada, antes de sua aplicação a dados reais. O dataset é composto por variáveis que representam características ambientais, de cultivo e geográficas, culminando em uma variável alvo que indica o risco de estresse hídrico.

## Variáveis Utilizadas

### Variáveis Numéricas
*   `ndvi`: Normalized Difference Vegetation Index. Um indicador da saúde e densidade da vegetação, variando de -1 a 1 (normalmente 0 a 1 para vegetação saudável).
*   `soil_moisture`: Umidade do solo em porcentagem ou escala similar.
*   `temperature`: Temperatura ambiente em graus Celsius.
*   `rainfall`: Quantidade de chuva acumulada em milímetros.
*   `humidity`: Umidade relativa do ar em porcentagem.
*   `wind_speed`: Velocidade do vento em km/h ou m/s.
*   `solar_radiation`: Radiação solar incidente em W/m².
*   `irrigation_hours`: Horas de irrigação aplicadas.

### Variáveis Categóricas
*   `crop_type`: Tipo de cultura agrícola (ex: Soy, Corn, Cotton).
*   `region`: Região agrícola simulada (ex: North, South, West).

### Variável Alvo
*   `stress_risk`: Nível de risco de estresse hídrico (categórica: Low Risk, Medium Risk, High Risk).

---

# Metodologia Utilizada

O pipeline de Machine Learning foi estruturado em etapas claras e sequenciais para garantir robustez, replicabilidade e desempenho otimizado:

## 1. Geração dos Dados
Nesta etapa inicial, foi criado um dataset sintético abrangente, com o objetivo de simular cenários agrícolas diversificados. O dataset incorpora:
*   Informações climáticas (temperatura, umidade, precipitação, radiação solar, velocidade do vento).
*   Umidade do solo, um fator crucial na determinação do estresse hídrico.
*   Índices de vegetação (NDVI), refletindo a saúde e vigor da cultura.
*   Tipo de cultura e região agrícola, para introduzir variabilidade e representatividade.

---

## 2. Feature Engineering e Pré-processamento
Para preparar os dados para os modelos de Machine Learning, foram aplicadas técnicas de engenharia e transformação de atributos:
*   **Separação entre variáveis numéricas e categóricas**: Essencial para aplicar transformações específicas para cada tipo de dado.
*   **One-Hot Encoding**: Converte variáveis categóricas em um formato numérico que pode ser compreendido pelos algoritmos.
*   **Normalização de atributos**: Escala as variáveis numéricas para uma faixa comum, evitando que atributos com grandes valores dominem o treinamento.
*   **Construção de pipelines reutilizáveis**: Utilização de `ColumnTransformer` do Scikit-Learn para encapsular e padronizar as etapas de pré-processamento.

---

## 3. Treinamento e Avaliação dos Modelos
Nesta fase, os modelos preditivos foram treinados e avaliados.
*   Os modelos foram treinados utilizando pipelines completos, que integram as etapas de pré-processamento diretamente ao treinamento, garantindo consistência e minimizando erros.
*   A avaliação foi realizada com métricas robustas para classificação, garantindo uma análise completa do desempenho.

---

# Modelos Testados

Para este projeto, foram selecionados e comparados dois modelos de Machine Learning amplamente reconhecidos por seu desempenho e versatilidade em problemas de classificação:

## 🌲 Random Forest Classifier

O Random Forest é um algoritmo de ensemble que constrói múltiplas árvores de decisão durante o treinamento e gera a previsão que é o modo das classes (para classificação) ou a média das previsões (para regressão) das árvores individuais.

### Vantagens
*   **Robustez a Overfitting**: A combinação de múltiplas árvores reduz o risco de sobreajuste.
*   **Boa Generalização**: Apresenta excelente desempenho em dados não vistos.
*   **Interpretação Simples**: A importância das características pode ser facilmente extraída.
*   **Lida bem com dados mistos**: Pode lidar com variáveis numéricas e categóricas.

---

## ⚡ XGBoost Classifier

XGBoost (eXtreme Gradient Boosting) é uma implementação otimizada de árvores de decisão aumentadas por gradiente, projetada para ser altamente eficiente, flexível e portátil. Ele é conhecido por seu alto desempenho em competições de Machine Learning.

### Vantagens
*   **Alto Desempenho**: Frequentemente alcança resultados de última geração em problemas de dados tabulares.
*   **Excelente Capacidade Preditiva**: Poderoso para capturar relações complexas nos dados.
*   **Eficiência e Velocidade**: Implementação otimizada para ser rápida e eficiente em termos de computação.
*   **Regularização Incorporada**: Ajuda a evitar o overfitting.

---

# Resultados Obtidos

Os modelos foram avaliados utilizando um conjunto de métricas de classificação para determinar seu desempenho na predição do risco de estresse hídrico. A tabela a seguir resume os resultados:

| Modelo          | Accuracy | Precision | Recall | F1-Score | ROC-AUC |
|-----------------|----------|-----------|--------|----------|---------|
| Random Forest   | 0.998    | 0.998     | 0.998  | 0.998    | 1.000   |
| XGBoost         | 1.000    | 1.000     | 1.000  | 1.000    | 1.000   |

---

# Melhor Modelo

Com base nas métricas de avaliação, o modelo **XGBoost Classifier** apresentou o melhor desempenho geral, atingindo 100% em todas as métricas consideradas:
*   Accuracy: 100%
*   Precision: 100%
*   Recall: 100%
*   ROC-AUC: 1.0

Este resultado demonstra a excelente capacidade do XGBoost em aprender os padrões complexos presentes no dataset sintético e fazer previsões altamente precisas para o risco de estresse hídrico.

---

# Interpretação com SHAP 🔍

Para aumentar a interpretabilidade do modelo e entender como as variáveis de entrada influenciam as previsões, foi utilizada a biblioteca **SHAP (SHapley Additive exPlanations)**. O SHAP atribui a cada característica uma importância para uma previsão individual, baseando-se nos valores de Shapley da teoria dos jogos cooperativos.

## Objetivos do SHAP
*   **Explicar previsões individuais**: Entender o porquê de uma determinada previsão para uma instância específica.
*   **Identificar variáveis globais relevantes**: Determinar quais características são as mais importantes para o modelo de forma geral.
*   **Aumentar a transparência do pipeline**: Tornar o processo de tomada de decisão do modelo mais compreensível e confiável.

---

## Features Mais Importantes

A análise SHAP revelou as características com maior impacto nas previsões do modelo XGBoost:

| Feature           | Importância (média do valor absoluto SHAP) |
|-------------------|--------------------------------------------|
| soil_moisture     | 3.53                                       |
| temperature       | 0.89                                       |
| region_north      | 0.04                                       |
| humidity          | 0.03                                       |
| crop_type_cotton  | 0.03                                       |

---

## Insights Obtidos da Análise SHAP

*   **Soil Moisture (Umidade do Solo)**: É, de longe, a característica mais crítica. Baixos níveis de umidade do solo aumentam significativamente o risco de estresse hídrico, um insight fundamental e esperado para a agricultura.
*   **Temperature (Temperatura)**: Temperaturas elevadas são o segundo fator mais importante, contribuindo para o aumento do estresse nas culturas devido ao aumento da evapotranspiração.
*   **Humidity (Umidade do Ar)**: Ambientes com baixa umidade relativa do ar (ambientes secos) aumentam a perda de água das plantas, elevando o risco de estresse.
*   **Region_North e Crop_Type_Cotton**: Embora com menor impacto que umidade e temperatura, indicam que a região e o tipo específico da cultura (neste caso, algodão) também possuem alguma influência no risco de estresse hídrico.

Esses insights são cruciais para a validação do modelo e para informar estratégias de manejo agrícola.

---

# Tecnologias Utilizadas

Este projeto foi desenvolvido utilizando uma stack tecnológica robusta e amplamente utilizada na comunidade de ciência de dados e Machine Learning:

*   **Python**: Linguagem de programação principal.
*   **Pandas**: Biblioteca para manipulação e análise de dados.
*   **NumPy**: Biblioteca para computação numérica e operações com arrays.
*   **Scikit-Learn**: Biblioteca para Machine Learning, incluindo pré-processamento e modelos.
*   **XGBoost**: Framework de gradient boosting para algoritmos de árvore.
*   **SHAP**: Biblioteca para interpretação de modelos de Machine Learning (Explainable AI).
*   **Matplotlib**: Biblioteca para criação de gráficos e visualizações de dados.
*   **Joblib**: Biblioteca para serialização e desserialização de objetos Python (salvar e carregar modelos).
*   **Streamlit**: Framework para construir aplicações web interativas de ciência de dados.

---

# Como Utilizar a Aplicação Web 🚀

A aplicação foi desenvolvida com **Streamlit** e oferece uma interface intuitiva para simular cenários agrícolas e prever o nível de risco de estresse hídrico em tempo real, utilizando o modelo de Inteligência Artificial treinado. O usuário pode ajustar diversas variáveis ambientais e agrícolas diretamente pela interface para explorar diferentes cenários e entender o impacto de cada fator.

## Link da Aplicação 🌐

Você pode acessar a aplicação online através do seguinte link:

```text
https://space-intelligence-platform-ai.onrender.com/
```

> ⚠️ **Observação:** A aplicação está hospedada no plano gratuito do Render. Por esse motivo, o primeiro acesso pode demorar alguns segundos ou até alguns minutos para carregar completamente. Isso ocorre porque a infraestrutura precisa inicializar o servidor e carregar todos os componentes da aplicação antes de disponibilizá-la ao usuário. Após a inicialização inicial, os acessos subsequentes tendem a ser significativamente mais rápidos.

## Interface da Aplicação

Ao abrir a aplicação, você será apresentado a uma interface amigável com campos interativos (sliders, caixas de seleção) para preenchimento e ajuste dos dados agrícolas.

## Variáveis Disponíveis para Simulação

A interface da aplicação permite configurar as seguintes variáveis:

### 🌿 NDVI
*   **Descrição**: Normalized Difference Vegetation Index. É um índice que mede a saúde, o vigor e a densidade da vegetação.
*   **Faixa**: `0.0` a `1.0`
*   **Interpretação**:
    *   Valores maiores (próximos a 1.0) indicam vegetação mais densa e saudável.
    *   Valores menores (próximos a 0.0) podem indicar vegetação rala, degradação ou estresse.

---

### 💧 Soil Moisture
*   **Descrição**: Representa a umidade do solo, um fator direto na disponibilidade de água para as plantas.
*   **Faixa**: `0` a `100` (em uma escala percentual ou relativa)
*   **Interpretação**:
    *   Valores baixos (próximos a 0) aumentam drasticamente o risco de estresse hídrico.
    *   Valores altos (próximos a 100) indicam maior disponibilidade de água e menor risco de estresse por seca.

---

### 🌡️ Temperature
*   **Descrição**: Temperatura ambiente em graus Celsius.
*   **Faixa**: `0` a `50` °C
*   **Interpretação**: Temperaturas elevadas podem aumentar a taxa de evapotranspiração das plantas, contribuindo para um maior risco de perda hídrica e estresse nas culturas.

---

### 🌧️ Rainfall
*   **Descrição**: Quantidade de chuva acumulada em um período.
*   **Faixa**: `0` a `300` mm
*   **Interpretação**: Baixos níveis de precipitação podem impactar diretamente a disponibilidade de água para as plantações, elevando o risco de estresse.

---

### 💨 Humidity
*   **Descrição**: Umidade relativa do ar em porcentagem.
*   **Faixa**: `0` a `100` %
*   **Interpretação**: Ambientes com umidade muito baixa (secos) aumentam a evapotranspiração das plantas, acelerando a perda de água e o potencial de estresse hídrico.

---

### 🌱 Crop Type
*   **Descrição**: Tipo de cultura agrícola que está sendo analisada.
*   **Opções disponíveis**:
    *   Soy (Soja)
    *   Corn (Milho)
    *   Cotton (Algodão)

---

### 🌍 Region
*   **Descrição**: Região agrícola simulada, que pode influenciar padrões climáticos e de solo.
*   **Opções disponíveis**:
    *   North
    *   South
    *   West

---

## Como Fazer uma Predição na Aplicação

Siga os passos abaixo para interagir com a aplicação e obter previsões de risco de estresse hídrico:

### 1. Ajuste os parâmetros
Utilize os sliders, caixas de seleção e campos de entrada na interface para configurar o cenário agrícola desejado, alterando as variáveis ambientais e de cultura.

---

### 2. Aguarde a inferência do modelo
Após ajustar os parâmetros, a aplicação enviará automaticamente os dados de entrada para o modelo treinado em XGBoost, que realizará a inferência.

---

### 3. Visualize o resultado
A Inteligência Artificial retornará uma das seguintes classificações para o risco de estresse hídrico, exibida claramente na interface:

| Resultado       | Significado                                   |
| --------------- | --------------------------------------------- |
| **Low Risk**    | Baixo risco de estresse hídrico               |
| **Medium Risk** | Risco moderado de estresse hídrico            |
| **High Risk**   | Alto risco de estresse hídrico, exigindo atenção |

---

# Conclusão

Este projeto demonstra de forma abrangente como técnicas modernas de **Machine Learning**, **Explainable AI**, **processamento geoespacial** e **inteligência operacional** podem ser aplicadas de maneira eficaz para prever riscos agrícolas e apoiar decisões estratégicas em campo.

Além disso, o pipeline desenvolvido serve como um exemplo prático e modular de como componentes inteligentes podem compor infraestruturas tecnológicas maiores e mais complexas, como a **Space Intelligence Platform**. Ele ilustra o potencial de conectar dados espaciais, sensores físicos e algoritmos de IA em uma arquitetura operacional integrada, visando otimizar a gestão de recursos e aumentar a produtividade agrícola de forma sustentável.

---

# Autores

Este projeto foi desenvolvido pelos seguintes membros do grupo:

*   Davi Passanha de Sousa Guerra - RM551605
*   Cauã Gonçalves de Jesus - RM97648
*   Luan Silveira Macea - RM98290
*   Rui Amorim Siqueira - RM98436
*   Luigi Ferrara Sinno - RM98047
