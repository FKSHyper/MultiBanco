import datetime
from dados import guardar_dados

# Função que permite transferir dinheiro entre duas contas registadas no dicionário
def realizar_transferencia(id_conta, contas):
    try:
        destino = input("ID da conta de destino: ")
        # Validação: A conta destino deve existir e não pode ser a própria conta do utilizador
        if destino not in contas or destino == id_conta:
            print("Erro: Conta de destino inválida.")
            return

        valor = float(input("Valor a transferir: "))

        # Verifica se o valor é positivo e se há saldo suficiente para a operação
        if 0 < valor <= contas[id_conta]['saldo']:
            contas[id_conta]['saldo'] -= valor
            contas[destino]['saldo'] += valor

            # Registo para quem envia
            contas[id_conta]['movimentos'].append({
                "data": datetime.datetime.now().strftime("%d/%m/%Y %H:%M"),
                "tipo": "Transferência (Saída)",
                "valor": valor,
                "destino": destino
            })

            guardar_dados(contas) # Atualizar ficheiro
            print(f"Transferência de {valor}€ para conta {destino} realizada!")
        else:
            print("Erro: Saldo insuficiente ou valor inválido.")

    except ValueError:
        print("Erro: Entrada inválida.")

# Função que realiza a retirada de dinheiro, respeitando o limite mínimo de 10€
def levantamento(id_conta, contas):
    try:
        print("\n--- LEVANTAMENTO ---")
        valor = float(input("Valor a levantar: "))

        # Validações de negócio
        if valor <= 0:
            print("Erro: O valor deve ser positivo.")
        elif valor > contas[id_conta]['saldo']:
            print("Erro: Saldo insuficiente!")
        elif valor < 10:
            print("Erro: O valor mínimo é 10€.")
        else:
            contas[id_conta]['saldo'] -= valor # Atualiza o saldo

            # Registo do movimento
            novo_movimento = {
                "data": datetime.datetime.now().strftime("%d/%m/%Y %H:%M"),
                "tipo": "Levantamento",
                "valor": valor,
                "destino": "-"
            }
            contas[id_conta]['movimentos'].append(novo_movimento)

            guardar_dados(contas) # Atualizar ficheiro
            print(f"Sucesso! Levantou {valor}€. Saldo atual: {contas[id_conta]['saldo']}€")

    except ValueError:
        print("Erro: Introduza um valor numérico válido.")

# Função que adiciona um valor ao saldo da conta ativa e regista o movimento
def realizar_deposito(id_conta, contas):
    try:
        valor = float(input("Valor a depositar: "))
        # Verifica se o valor é positivo
        if valor <= 0:
            print("Erro: O valor deve ser positivo.")
        else:
            contas[id_conta]['saldo'] += valor

            # Registo do depósito no histórico
            mov = {
                "data": datetime.datetime.now().strftime("%d/%m/%Y %H:%M"),
                "tipo": "Depósito",
                "valor": valor,
                "destino": "-"
            }
            contas[id_conta]['movimentos'].append(mov)

            guardar_dados(contas) # Atualizar ficheiro
            print(f"Depósito realizado! Novo saldo: {contas[id_conta]['saldo']}€")

    except ValueError:
        print("Erro: Valor inválido.")

# Função que exibe de forma formatada o nome do titular e o saldo disponível
def consultar_saldo(id_conta, contas):
    saldo = contas[id_conta]['saldo']
    print("\n" + "="*20)
    print(f" TITULAR: {contas[id_conta]['nome']}")
    print(f" SALDO ATUAL: {saldo:.2f}€")
    print("="*20)

# Função que lista todos os movimentos registados na conta
def consultar_movimentos(id_conta, contas):
    print("\n--- HISTÓRICO DE MOVIMENTOS ---")
    movimentos = contas[id_conta].get('movimentos', [])
    # Verifica se existem movimentos
    if not movimentos:
        print("Sem movimentos registados.")
    else:
        for m in movimentos:
            print(f"{m['data']} | {m['tipo']:<15} | {m['valor']:>8.2f}€")

# Menu Principal
def menu_principal(id_conta, contas):
    while True:
        print("\n" + "=" * 30)
        print(f"--- MENU CLIENTE ({contas[id_conta]['nome']}) ---")
        print("=" * 30)
        print(
            "1. Consultar Saldo\n2. Realizar Levantamento\n3. Realizar Depósito\n4. Realizar Transferência\n5. Consultar Movimentos\n6. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            consultar_saldo(id_conta, contas)
        elif opcao == "2":
            levantamento(id_conta, contas)
        elif opcao == "3":
            realizar_deposito(id_conta, contas)
        elif opcao == "4":
            realizar_transferencia(id_conta, contas)
        elif opcao == "5":
            consultar_movimentos(id_conta, contas)
        elif opcao == "6":
            print("A sair... Volte sempre!")
            break