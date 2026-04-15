import datetime
from utilitarios import validar_nome, validar_pin, validar_id_conta
from dados import guardar_dados

# Função para criar clientes
def criar_cliente(contas):
    print("\n--- REGISTAR NOVO CLIENTE ---")

    num_conta = validar_id_conta(contas, novo = True)
    nome_validado = validar_nome()
    pin_validado = validar_pin()

    # Criar estrutura
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
    print(f"Conta {num_conta} criado com sucesso para {nome_validado}!")

# Função para listar clientes
def listar_clientes(contas):
    print("\n--- LISTA DE CLIENTES ---")

    # Verificação se existem contas registadas
    if not contas:
        print("Não existemcontas registadas")
        return

    # Ciclo para listar as informações de todas as contas
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

# Função para mostrar as estatísticas na forma de um relatório
def mostrar_estat(contas):
    print("\n" + "=" * 30)
    print("--- Relatório Administrativo ---")
    print("=" * 30)

    # Inicialização
    total_banco = 0.0
    total_movimentos = 0
    total_clientes = len(contas)

    # Verificação se existe clientes registrados
    if total_clientes == 0:
        print("O banco não tem clientes registrados!")
        return

    # Ciclo para sumar o total de saldo e movimentos
    for id_conta, info in contas.items():
        total_banco += info['saldo']
        total_movimentos += len(info['movimentos']) # Soma o número de itens

    # Relatório Administrativo
    print(f"Saldo Total no Banco:       {total_banco:>.2f} €")
    print(f"Número de Cientes:          {total_clientes}")
    print(f"Total de Operações:         {total_movimentos}")
    print(f"Média por Cliente:          {(total_banco / total_clientes):>.2f} €")
    print("=" * 30)

# Função que permite o ADMIN pesquisar todos os movimentos de uma conta em específico
def pesquisar_historico(contas):
    print("\n--- PESQUISA DE MOVIMENTOS ---")
    print("=" * 30)

    # Validar ID Conta
    id_conta = validar_id_conta(contas, novo = False)

    # Verificação para mostrar o histórico
    if id_conta:
        historico = contas[id_conta]['movimentos']
        print(f"\nHistórico da Conta: {id_conta} ({contas[id_conta]['nome']})")
        print(f"{'Data':<20} | {'Tipo':<12} | {'Valor':<10} | {'Destino'}")
        print("=" * 60)

        for m in historico:
            print(f"{m['data']:<20} | {m['tipo']:<12} | {m['valor']:>8.2f}€ | {m['destino']}")

# Menu ADMIN
def menu_admin(contas):
    while True:
        print("\n--- MENU ADMIN ---")
        print("1. Criar Cliente")
        print("2. Listar Cliente")
        print("3. Listar/Pesquisar movimentos")
        print("4. Delete Cliente")
        print("5. Estatísticas")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            criar_cliente(contas)
        elif opcao == "2":
            listar_clientes(contas)
        elif opcao == "3":
            pesquisar_historico(contas)
        elif opcao == "4":
            eliminar_cliente(contas)
        elif opcao == "5":
            mostrar_estat(contas)
        elif opcao == "6":
            print("A sair do modo administrativo...")
            break
        else:
            print("Opção inválida!")