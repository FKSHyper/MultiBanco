import dados
import admin
import utilizador
from utilitarios import realizar_login

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

def main():
    contas = dados.carregar_dados()

    #Logica Menus






























