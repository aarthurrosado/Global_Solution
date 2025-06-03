
import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

from dados_sensores import _criar_dados  # import da função
df = _criar_dados()

st.title("Analise de dados")
st.subheader("Visualização dos dados")
st.dataframe(df.tail())
linhas, colunas = df.shape
st.write(f"o data frame possui {linhas} linhas e {colunas} colunas")
df_types = pd.DataFrame({
    'Coluna': df.columns,
    'Tipos de Dados': df.dtypes.astype(str)
})
st.write(df_types)
# Verificar valores ausentes
st.subheader('Valores Ausentes')
st.write(df.isnull().sum())
st.write("Analise descritiva dos dados:")
st.write(df.describe())

#analise grafica
st.title("Contagem de risco")
contagem_risco = df['Nivel de Risco'].value_counts()

fig, ax = plt.subplots()
contagem_risco.plot(kind='bar', color=['green', 'orange', 'red'], ax=ax)
ax.set_title('Distribuição dos Níveis de Risco')
ax.set_ylabel('Quantidade')
ax.set_xlabel('Nível de Risco')
st.pyplot(fig)
print(df.columns)
df['Chuva'] = df['Chuva'].map({'Sem chuva': 0, 'Chovendo': 1})
df['Nivel de Risco'] = df['Nivel de Risco'].map({'Baixo': 0, 'Médio': 1, 'Alto': 2})
df['Tipo de Solo'] = df['Tipo de Solo'].map({'Arenoso': 0, 'Argiloso': 1, 'Rochoso': 2})
df['Inclinação'] = df['Inclinação'].map({'Leve': 0, 'Moderada': 1, 'Forte': 2})
df['Região'] = df['Região'].map({'A': 0, 'B': 1,'C': 2, 'D': 3})
st.title("Matriz de correlação")
correlacao = df.corr()
fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(correlacao, annot=True, cmap='coolwarm', ax=ax)
st.pyplot(fig)
