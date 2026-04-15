import dados
import admin
import utilizador
from utilitarios import realizar_login

# MAIN
def main():
    contas = dados.carregar_dados()

    # Garantia de admin inicial
    if not contas:
        contas = {"0000": {"nome": "Admin", "pin": "0000", "tipo": "admin", "saldo": 0.0, "movimentos": []}}

    id_logado = realizar_login(contas)

    if id_logado:
        if id_logado == "Admin" or contas[id_logado].get('tipo') == 'admin':
            admin.menu_admin(contas)  # Chama o menu que está no admin.py
        else:
            utilizador.menu_principal(id_logado, contas)  # Chama o menu no utilizador.py

    dados.guardar_dados(contas)


if __name__ == "__main__":
    main()