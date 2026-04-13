import json
import os

# Estrutura Principal

banco_dados = {
    "1001": {
        "nome": "João Silva",
        "pin": "1234",
        "saldo": 1000.0,
        "movimentos": [
            {"data": "2023-10-27 10:30", "tipo": "Abertura", "valor": 1000.0, "destino": "-"}
        ]
    },
    "1002": {
        "nome": "Maria Santos",
        "pin": "4321",
        "saldo": 1000.0,
        "movimentos": []
    }
}
#Ciclo para listar todos os clientes
#for conta, info in banco_dados.item():
#    print(f"Conta: {conta} | Titular: {info['nome']} | Saldo: {info['saldo']}€")

# Nome do ficheiro: "dados_banco.json"

#Função para guardar dados no ficheiro Json
def guardar_dados(dados):
    try:
        with open('dados_banco.json', 'w') as ficheiro:
            json.dump(dados, file, indent=4, ensure_ascii=False)

        print("Sistema: Dados sincronizados no ficheiro com sucesso")
    except Exception as e:
        print(f"Erro critico ao guardar dados: {e}")

#Função para carregar o dicionário do ficheiro Json para o código
def carregar_dados():
    if not os.path.exists('dados_banco.json'):
        print("Ficheiro não encontrado. A iniciar base de dados vazia")
        return {}
    try:
        with open('dados_banco.json', 'r') as ficheiro:
            return json.load(ficheiro)
    except Exception as e:
        print(f"Erro critico ao carregar dados: {e}")
        return {}