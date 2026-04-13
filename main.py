# Import - Implementar Persistênciia
import json
import os
# Import - Menu ADMIN
import datetime

# Estrutura Principal


# !!Estrutura de Dados!!#
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


# !!Implementar a Persistência!!#

# Nome do ficheiro: "dados_banco.json"

# Função para guardar dados no ficheiro Json
def guardar_dados(dados):
    try:
        with open('dados_banco.json', 'w') as ficheiro:
            json.dump(dados, file, indent=4, ensure_ascii=False)

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

# Função para validar nome inserido
def validar_nome():
    while True:
        nome = input("Nome do Titular: ")

        # Verificação se é apenas letras e remove espaços
        if nome.replace(" ", "").isalpha() and len(nome) > 0:
            return nome.title()
        else:
            print("ERRO: O nome deve conter apenas letras e não estar vazio!")

# Função para validar PIN inserido
def validar_pin():
    while True:
        pin = input("Defina o PIN (4 dígitos): ")
        if len(pin) == 4 and pin.isdigit():
            return pin
        else:
            print("ERRO: O PIN deve ter exatamente 4 números!")

# Função para validar o ID da Conta
def validar_id_conta(contas, novo = True):
    while True:
        id_conta = input("ID do Conta: ").strip()

        if id_conta.isdigit():
            print("ERRO: O ID da conta deve conter apenas números!")
            continue

        if novo:
            if id_conta in contas:
                print(f"ERRO: A conta {id_conta} já existe no sistema!")
            else:
                return id_conta

        else:
            if id_conta not in contas:
                print(f"ERRO: A conta {id_conta} não foi encontrada!")
            else:
                return id_conta

# Menu ADMIN

# Função para criar clientes
def criar_cliente(contas):
    print("\n--- REGISTAR NOVO CLIENTE ---")

    num_conta = validar_id_conta(contas, novo = True)
    nome_validado = validar_nome()
    pin_validado = validar_pin()

    #Criar estrutura
    contas[num_conta] = {
        "nome": nome_validado,
        "pin": pin_validado,
        "saldo": 1000.0,
        "movimentos": [
            { "data": datetime.datetime.now().strftime("%d/%m/%Y %H:%M"), "tipo": "Abertura", "valor": 1000.0, "destino": "-" }
        ]
    }

    #Guardar a conta no ficheiro
    guardar_dados(contas)
    print(f"Conta {num_conta} criado com sucesso para {nome}!")

# Função para listar clientes
def listar_clientes(contas):
    print("\n--- LISTA DE CLIENTES ---")

    # Verificação se existem contas registadas
    if not contas:
        print("Não existemcontas registadas")
        return

    #Ciclo para listar as informações de todas as contas
    for num, info in contas.items():
        print(f"ID: {num} | Titular: {info['nome']} | Saldo: {info['saldo']}€")

# Função para eliminar clientes
def eliminar_cliente(contas):
    print("\n--- ELIMINAR CLIENTE ---")

    num_conta = input("Número da conta a eliminar: ")

    # Verificação se a conta existe
    if num_conta in contas:
        confirmar = input(f"Tem a certeza que quer eliminar a conta de {contas[num_conta]['nome']} ? (S/N): ")
        #Verificação da confirmação se quer eliminar
        if confirmar.lower() == "s":
            del contas[num_conta]
            guardar_dados(contas) # Atualizar o ficheiro
            print("Conta eliminada com sucesso!")
        else:
            print("Conta não encontrada!")



































