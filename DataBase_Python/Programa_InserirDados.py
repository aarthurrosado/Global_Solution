
import pandas as pd
import oracledb
import sys

# Conexão
DSN = "oracle.fiap.com.br:1521/ORCL"
USER = "RM562061"
PASSWORD = "240805"

# Função para conectar
def obter_conexao():
    try:
        conn = oracledb.connect(user=USER, password=PASSWORD, dsn=DSN)
        cursor = conn.cursor()
        return conn, cursor
    except Exception as exc:
        print(f"Erro ao conectar no banco: {exc}")
        return None, None

conn, cursor = obter_conexao()
if conn is None:
    sys.exit(1)

# Caminho para o CSV
caminho_csv = "/content/dados.csv"

# Leitura do CSV
try:
    df = pd.read_csv(caminho_csv, encoding='utf-8')
except UnicodeDecodeError:
    df = pd.read_csv(caminho_csv, encoding='latin1')

# Renomear colunas e padronizar
df.columns = ['regiao', 'temperatura', 'umidade', 'tipo_solo', 'inclinacao', 'chuva', 'vibracao', 'risco', 'nivel_risco']

# Inserção de dados
try:
    for _, row in df.iterrows():
        cursor.execute("""
            INSERT INTO SENSORES_REGIAO (
                REGIAO, TEMPERATURA, UMIDADE, TIPO_SOLO,
                INCLINACAO, CHUVA, VIBRACAO, RISCO, NIVEL_RISCO
            ) VALUES (
                :1, :2, :3, :4, :5, :6, :7, :8, :9
            )
        """, (
            row['regiao'],
            float(row['temperatura']),
            float(row['umidade']),
            row['tipo_solo'],
            row['inclinacao'],
            row['chuva'],
            float(row['vibracao']),
            float(row['risco']),
            row['nivel_risco']
        ))

    conn.commit()
    print("Dados inseridos com sucesso!")

except Exception as e:
    print(f"Erro ao inserir dados: {e}")
    conn.rollback()

finally:
    if cursor: cursor.close()
    if conn: conn.close()
