# RenanMendes
# ArthurRosado


# Instalando os pacotes.
install.packages("readr")
install.packages("dplyr")
install.packages("ggplot2")
install.packages("readxl")
install.packages("writexl")
install.packages("psych")
install.packages("corrplot")
install.packages("ggpubr")

# Carregar bibliotecas necessárias
library(ggplot2)
library(dplyr)
library(tidyr)
library(corrplot)
library(ggpubr)
library(readr)

dados <- read_delim("C:/Users/renan.a.mendes/Downloads/dados.csv", delim = ",", locale = locale(decimal_mark = "."))


# Ver os dados
print(dados)


# Verificar nomes das colunas
print(colnames(dados))

# Renomear as colunas 
colnames(dados) <- c("Regiao", "Temperatura", "Umidade", "Tipo_Solo", 
                     "Inclinacao", "Chuva", "Vibracao", "Risco", "Nivel_Risco")

# Verificação
glimpse(dados)

# Estatísticas descritivas
summary(dados)

# Converter variáveis categóricas para fator
dados$Regiao <- as.factor(dados$Regiao)
dados$Tipo_Solo <- as.factor(dados$Tipo_Solo)
dados$Inclinacao <- as.factor(dados$Inclinacao)
dados$Chuva <- as.factor(dados$Chuva)
dados$Nivel_Risco <- as.factor(dados$Nivel_Risco)

# Correlação entre variáveis numéricas
num_vars <- dados %>%
  select(Temperatura, Umidade, Vibracao, Risco)

cor_matrix <- cor(num_vars)
print(cor_matrix)
corrplot(cor_matrix, method = "circle", tl.col = "black", tl.cex = 0.8)


# Calcular médias por região
medias_por_regiao <- dados %>%
  group_by(Regiao) %>%
  summarise(
    Temperatura_media = mean(Temperatura),
    Umidade_media = mean(Umidade),
    Vibracao_media = mean(Vibracao),
    Risco_medio = mean(Risco)
  )

# Mostrar resultados
print(medias_por_regiao)

# Plotar as médias de risco por região
ggplot(medias_por_regiao, aes(x = Regiao, y = Risco_medio, fill = Regiao)) +
  geom_bar(stat = "identity") +
  labs(title = "Risco Médio por Região", y = "Risco Médio") +
  theme_minimal()

# Temperatura Média por Região
ggplot(medias_por_regiao, aes(x = Regiao, y = Temperatura_media, fill = Regiao)) +
  geom_bar(stat = "identity") +
  labs(title = "Temperatura Média por Região", y = "Temperatura Média") +
  theme_minimal()


# Calcular a proporção de inclinação por região
proporcao_inclinacao <- dados %>%
  group_by(Regiao, Inclinacao) %>%
  summarise(Contagem = n(), .groups = "drop") %>%
  group_by(Regiao) %>%
  mutate(Proporcao = Contagem / sum(Contagem))

# Visualizar a tabela
print(proporcao_inclinacao)

# Plotar gráfico de barras empilhadas
ggplot(proporcao_inclinacao, aes(x = Regiao, y = Proporcao, fill = Inclinacao)) +
  geom_bar(stat = "identity", position = "fill") +
  scale_y_continuous(labels = scales::percent_format()) +
  labs(title = "Proporção de Inclinação por Região", y = "Proporção", x = "Região") +
  theme_minimal()


# Boxplot da temperatura por nível de risco
ggplot(dados, aes(x = Nivel_Risco, y = Temperatura, fill = Nivel_Risco)) +
  geom_boxplot() +
  labs(title = "Temperatura por Nível de Risco", y = "Temperatura (°C)", x = "Nível de Risco") +
  theme_minimal()

# Gráfico de barras da frequência por tipo de solo
ggplot(dados, aes(x = Tipo_Solo, fill = Tipo_Solo)) +
  geom_bar() +
  labs(title = "Distribuição por Tipo de Solo", x = "Tipo de Solo", y = "Frequência") +
  theme_minimal()

# Gráfico de dispersão: Umidade vs Risco
ggplot(dados, aes(x = Umidade, y = Risco, color = Nivel_Risco)) +
  geom_point(size = 3) +
  labs(title = "Umidade vs Risco", x = "Umidade (%)", y = "Nível de Risco") +
  theme_minimal()

# Facet: risco por região e chuva
ggplot(dados, aes(x = Regiao, y = Risco, fill = Chuva)) +
  geom_bar(stat = "identity", position = "dodge") +
  labs(title = "Risco por Região e Condição de Chuva", y = "Risco") +
  theme_minimal()
