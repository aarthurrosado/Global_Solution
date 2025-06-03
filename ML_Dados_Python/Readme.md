#  Modelo de Risco de Deslizamento

---

##  Análise Exploratória dos Dados

A aplicação começa com uma análise descritiva completa dos dados simulados, composta por 5000 observações com 9 variáveis, incluindo:

- Temperatura
- Umidade
- Tipo de Solo
- Inclinação
- Chuva
- Vibração
- Risco (valor contínuo)
- Nível de Risco (categórico)

###  Verificação de Valores Ausentes
Todos os campos do conjunto de dados foram verificados e **não possuem valores nulos**.

###  Tipos de Dados
A estrutura dos dados envolve tanto variáveis contínuas (`float64`) quanto categóricas (`object`), com tratamento apropriado por codificação durante o processamento.

---

##  Matriz de Correlação

Foi construída uma **matriz de correlação de Pearson** para identificar relações entre as variáveis:

- A variável "Umidade" apresentou alta correlação com o "Risco" (`0.63`) e com o "Nível de Risco" (`0.53`).
- A variável "Chuva" também teve influência significativa, com correlação de `0.54` com o risco.
- A variável "Inclinação" teve correlação moderada.

Esses dados ajudam a compreender **quais variáveis são mais influentes na modelagem preditiva**.

---

##  Distribuição do Nível de Risco

O dataset foi balanceado da seguinte forma:

- Baixo: maior parte das amostras.
- Médio: também presente em grande quantidade.
- Alto: representando os casos mais raros.

Essa distribuição reflete cenários mais comuns na natureza, com deslizamentos severos sendo eventos menos frequentes, mas críticos.

---

##  Modelo Preditivo

Foi utilizado um modelo de regressão baseado em **Random Forest Regressor** da biblioteca scikit-learn para prever o valor contínuo de risco.

### Métricas de Avaliação

| Métrica         | Valor Treino | Valor Teste |
|-----------------|--------------|-------------|
| R²              | 0.92         | 0.89        |
| MAE (Erro médio)| 0.30         | 0.37        |

>  Acurácia (R² Teste: 0.89) indica um modelo com boa capacidade preditiva.


Apesar do R² de treino ser ligeiramente maior, a diferença entre treino e teste é pequena:

- Isso mostra que o modelo generaliza bem para dados novos.
- O **erro médio absoluto (MAE) também se mantém estável entre treino e teste, reforçando que não há overfitting.

---

Com base na random florest, as variáveis com maior importância na previsão foram:

1. Umidade
2. Chuva
3. Inclinação

Isso reforça o valor preditivo das condições meteorológicas e geográficas na ocorrência de deslizamentos.



