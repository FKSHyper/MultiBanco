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
        # Verificação se o PIN tem 4 números e se é números
        if len(pin) == 4 and pin.isdigit():
            return pin
        else:
            print("ERRO: O PIN deve ter exatamente 4 números!")

# Função para validar o ID da Conta
def validar_id_conta(contas, novo = True):
    while True:
        id_conta = input("ID da Conta: ").strip() # Remove espaços no ínicio e fim

        # Verificar se está vazio
        if not id_conta:
            print("ERRO: O ID não pode estar vazio!")
            continue

        # Verificação se o ID da conta tem letras
        if not id_conta.isdigit():
            print("ERRO: O ID da conta deve conter apenas números!")
            continue

        # Se novo for verdadeiro
        if novo:
            # Verifica se já existe a conta
            if id_conta in contas:
                print(f"ERRO: A conta {id_conta} já existe no sistema!")
            else:
                return id_conta
        # Se novo for falso
        else:
            # Verificação se a conta não existe
            if id_conta not in contas:
                print(f"ERRO: A conta {id_conta} não foi encontrada!")
            else:
                return id_conta

# Função para o cliente realizar login
def realizar_login(contas):
    print("\n" + "=" * 30)
    print("--- ACESSO AO SISTEMA ---")
    print("=" * 30)

    # Validação de ID
    id_conta = validar_id_conta(contas, novo = False)

    # Verificação se o ID é None
    if id_conta is None:
        return None

    tentativas = 3
    while tentativas > 0:
        print(f"\nTentativas restantes: {tentativas}")

        # Validações
        nome_inserido = validar_nome()
        pin_inserido = validar_pin()
        dados_reais = contas[id_conta]

        # Verificação final contra os dados guardados
        if dados_reais['nome'] == nome_inserido and dados_reais['pin'] == pin_inserido:
            print(f"Sucesso! Bem-vindo {nome_inserido}!")
            return id_conta
        else:
            tentativas -= 1
            print("Nome ou PIN não coincidem com os registos!")

    print("\nProcesso cancelado por excesso de erros!")
    return None