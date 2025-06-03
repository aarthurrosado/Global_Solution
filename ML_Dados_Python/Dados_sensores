
# Bibiliotecas Usadas
import numpy as np
import pandas as pd
import streamlit as st
import time

@st.cache_data(show_spinner=True)
def _criar_dados(n_samples= 5000):
    np.random.seed(999)
    time.sleep(2)
    print("Carregando data set. . .")

    temperatura = np.random.normal(loc= 28, scale= 4, size=n_samples)
    Umidade = np.random.uniform(low= 40, high= 80, size=n_samples )
    Chuva = np.random.choice(['Sem chuva', 'Chovendo'], size=n_samples, p=[0.6, 0.4])
    acc_x = np.random.normal(loc=0, scale=0.3, size=n_samples)
    acc_y = np.random.normal(loc=0, scale=0.3, size=n_samples)
    acc_z = np.random.normal(loc=9.81, scale=0.4, size=n_samples)
    vibracao_total = np.sqrt(acc_x ** 2 + acc_y ** 2 + (acc_z - 9.81) ** 2)

    # Variáveis categóricas
    Regiao = np.random.choice(['A', 'B', 'C', 'D'], size=n_samples)
    Inclinacao_terreno = np.random.choice(['Leve', 'Moderada', 'Forte'], size=n_samples, p=[0.3, 0.4, 0.3])
    tipo_solo = np.random.choice(['Arenoso', 'Argiloso', 'Rochoso'], size=n_samples, p=[0.3, 0.45, 0.25])

    mapa_Inclinacao = {'Leve': 1.05, 'Moderada': 1.35, 'Forte': 1.5}
    mapa_solo = {'Arenoso': 1.35, 'Argiloso': 1.10, 'Rochoso': 0.95}
    mapa_chuva = {'Sem chuva': 0, 'Chovendo': 1.8}

    #efeitos
    efeito_inclinacao = np.vectorize(mapa_Inclinacao.get)(Inclinacao_terreno)
    efeito_solo = np.vectorize(mapa_solo.get)(tipo_solo)
    efeito_chuva = np.vectorize(mapa_chuva.get)(Chuva)

    risco = (
        (temperatura - 20) * 0.015 +
        (Umidade - 50) * 0.05 +
        vibracao_total * 1.2 +
        efeito_chuva
    ) * efeito_inclinacao * efeito_solo

    risco += np.random.normal(loc=0, scale=0.4, size=n_samples)
    risco = np.clip(risco, a_min=0, a_max=None)

    nivel_risco = np.where(risco < 2.5, 'Baixo',
                           np.where(risco < 4.5, 'Médio', 'Alto'))
    # Criando o DataFrame final
    df = pd.DataFrame({
        'Região': Regiao,
        'Temperatura': temperatura,
        'Umidade': Umidade,
        'Tipo de Solo': tipo_solo,
        'Inclinação': Inclinacao_terreno,
        'Chuva': Chuva,
        'Vibração': vibracao_total,
        'Risco': risco,
        'Nivel de Risco': nivel_risco
    })
    return df
