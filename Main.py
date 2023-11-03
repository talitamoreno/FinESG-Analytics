# Importar bibliotecas para integração de dados ESG
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Etapa 1: Coleta de Dados
# Suponha que você já tenha coletado os dados e eles estão em arquivos CSV separados.
dados_clientes = pd.read_csv("dados_clientes.csv")
dados_financeiros = pd.read_csv("dados_financeiros.csv")
dados_esg = pd.read_csv("dados_esg.csv")

# Etapa 2: Pré-processamento de Dados
# Preencher valores nulos com a média da coluna "Idade"
dados_clientes["Idade"].fillna(dados_clientes["Idade"].mean(), inplace=True)

# Remover linhas com valores nulos em uma coluna específica
dados_clientes.dropna(subset=["Interesses"], inplace=True)

# Converter uma coluna de datas para o formato de data
dados_clientes["Data de Registro"] = pd.to_datetime(dados_clientes["Data de Registro"])

# Etapa 3: Análise Descritiva
# Calcule estatísticas básicas dos dados
estatisticas_descritivas = dados_clientes.describe()

# Crie gráficos para visualização
sns.histplot(dados_clientes["idade"])
plt.title("Distribuição de Idades")
plt.show()

# Etapa 4: Análise Exploratória de Dados (AED)
# Calcular a porcentagem de mulheres no conselho de administração
dados_esg["Diversidade de Gênero no Conselho"] = (dados_esg["Mulheres no Conselho"] / dados_esg["Total de Membros do Conselho"]) * 100

# Calcular a média de idade para cada perfil
media_idade = perfis_clientes.groupby("Perfil")["Idade"].mean()

# Etapa 5: Análise de Dados Financeiros
# Calcular o ROE (Retorno sobre o Patrimônio Líquido)
dados_financeiros["ROE"] = dados_financeiros["Lucro Líquido"] / dados_financeiros["Patrimônio Líquido"]

# Etapa 6: Análise de Critérios ESG
# Calcular a porcentagem de mulheres no conselho de administração
dados_esg["Diversidade de Gênero no Conselho"] = (dados_esg["Mulheres no Conselho"] / dados_esg["Total de Membros do Conselho"]) * 100

# Etapa 7: Conectando Insights entre Perfis de Clientes
# Calcular a média de idade para cada perfil
media_interesses = perfis_clientes.groupby("Perfil")["Interesses"].apply(lambda x: " ".join(x))
media_comportamento_financeiro = perfis_clientes.groupby("Perfil")["Comportamento_Financeiro"].apply(lambda x: " ".join(x))

# Modelagem Preditiva
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Suponha que "X" seja a idade dos clientes e "y" seja o comportamento financeiro.
X = dados_clientes["Idade"].values.reshape(-1, 1)
y = dados_clientes["Comportamento Financeiro"]

# Dividir os dados em conjuntos de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Criar e ajustar o modelo de regressão linear
modelo = LinearRegression()
modelo.fit(X_train, y_train)

# Fazer previsões
previsoes = modelo.predict(X_test)

# Avaliar o desempenho do modelo
mse = mean_squared_error(y_test, previsoes)
r2 = r2_score(y_test, previsoes)

# Imprimir resultados
print(f"Erro Quadrático Médio (MSE): {mse}")
print(f"R-squared (R2): {r2}")

# Salvar os resultados em um arquivo CSV
estatisticas_descritivas.to_csv("estatisticas_descritivas.csv", index=False)
