import json
import os

# Nome do ficheiro: "dados_banco.json"

# Função para guardar dados no ficheiro Json
def guardar_dados(dados):
    try:
        with open('dados_banco.json', 'w') as ficheiro:
            json.dump(dados, ficheiro, indent=4, ensure_ascii=False)

        print("Sistema: Dados sincronizados no ficheiro com sucesso")
    except Exception as e:
        print(f"Erro critico ao guardar dados: {e}")

# Função para carregar o dicionário do ficheiro Json para o código
def carregar_dados():
    # Verificação se o ficheiro existe
    if not os.path.exists('dados_banco.json'):
        print("Ficheiro não encontrado. A iniciar base de dados vazia")
        return {}

    try:
        with open('dados_banco.json', 'r') as ficheiro:
            return json.load(ficheiro)
    except Exception as e:
        print(f"Erro critico ao carregar dados: {e}")
        return {}
