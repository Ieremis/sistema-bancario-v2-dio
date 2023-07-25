def menu():
    menu = """
            === MENU ===

        Insira a opcao valida
        para realizar a operacao!

        [d] Realizar Depósito

        [s] Realizar Saque

        [e] Realizar Extrato

        [c] Cadastrar Usuario

        [cc] Cadastrar Conta Corrente

        [l] Listar Contas

        [q] Sair do Sistema

    """
    return input(menu)

def depositar(saldo, valor_para_deposito, mensagem_extrato, /):
    if valor_para_deposito > 0:
            print(f"R${valor_para_deposito:.2f} será depositado na sua conta!")
            saldo += valor_para_deposito
            mensagem_extrato += (f"Deposito no valor de +R${valor_para_deposito:.2f} \n\n")
            
    else: print("Insira um valor de deposito valido!!")
    return saldo, mensagem_extrato

def sacar(*, saldo, valor_para_saque, mensagem_extrato, limite_saque, saques_realizados):
    if valor_para_saque <= limite_saque and valor_para_saque > 0 and valor_para_saque <= saldo:
                print(f"{valor_para_saque:.2f} sera sacado da sua conta!")
                saldo -= valor_para_saque
                saques_realizados += 1
                mensagem_extrato += (f"Saque no valor de -R${valor_para_saque:.2f} \n\n")
                

    elif valor_para_saque <= 0: 
                print("Insira um valor de saque valido!!")
                
    elif valor_para_saque > limite_saque:
                print("Seu valor para saque esta acima do nosso limite de R$500.00")

    else: print("Voce nao possui esse valor disponivel em sua conta")
    return saldo, mensagem_extrato, saques_realizados

def extrato(saldo, /, *, mensagem_extrato):
    print("\n------------EXTRATO------------\n")
    if mensagem_extrato != "":
            print(mensagem_extrato)
            print("-------------------------------\n")
            print(f"Saldo em conta: R${saldo:.2f}\n")
            print("-------------------------------\n")
    else: 
            print("Não foram realizadas movimentações\n")
            print("-------------------------------\n")
            print(f"Saldo em conta: R${saldo:.2f}\n")
            print("-------------------------------\n")

def criar_usuario(lista_usuarios):
    print("Iniciando o procedimento de criação do usuário")
    print("Informe seus dados pessoais, por favor")
    cpf = input("Insira seu CPF (somente numeros): ")

    for usuario in lista_usuarios:
        if cpf == usuario["CPF"]:
            print("CPF já cadastrado no sistema!")
            return

    nome = input("Insira seu nome completo: ")
    data_de_nascimento = input("Insira sua data de nascimento (dd-mm-aa): ")
    print("Agora informe seu endereço, por favor")
    logradouro = input("Insira o logradouro da sua residência: ")
    nro = input("Insira o numero da sua residencia: ")
    bairro = input("Insira o nome do bairro: ")
    cidade = input("Insira sua cidade: ")
    sigla_estado = input("Insira a sigla do seu estado: ")
    endereco = (f"Logradouro: {logradouro}, N {nro} - Bairro: {bairro} - Cidade/Estado: {cidade}/{sigla_estado}")
    lista_usuarios.append({
        "CPF":cpf,
        "Nome do Usuario":nome,
        "Data de Nascimento":data_de_nascimento,
        "Endereço":endereco
    })

def criar_conta(lista_contas, lista_usuarios):
    print("Iniciando o procedimento de criação da conta corrente")
    cpf = input("Insira seu CPF (somente numeros): ")

    for usuario in lista_usuarios:
        if cpf == usuario["CPF"]:
            lista_contas.append({
                "Agencia":"0001",
                "Numero da conta":len(lista_contas) + 1,
                "Usuario":usuario,
            })
            print("Conta criada com sucesso!")
            return
        
    print("Usuário nao cadastrado no sistema")

def listar_contas(lista_contas):
    for conta in lista_contas:
        print(f"""
                Agencia: {conta["Agencia"]}
                C/C: {conta["Numero da conta"]}
                Usuario: {conta["Usuario"]["Nome do Usuario"]}
            \n==================================================
            \n""")

def main():
    
    LIMITE_SAQUE = 500
    LIMITE_DIARIO = 3
    saques_realizados = 0
    saldo = 0
    mensagem_extrato = ""
    lista_usuarios = []
    lista_contas = []

    while True:
        
        opcao = menu()
        
        if opcao == "d":
            print("Iniciando operação de Depósito")
            valor_para_deposito = float(input("Insira um valor para ser depositado: "))

            saldo, mensagem_extrato = depositar(saldo, valor_para_deposito, mensagem_extrato)

        elif opcao == "s":
            if(saques_realizados < LIMITE_DIARIO):
                print("Iniciando operacao de Saque")
                valor_para_saque = float(input("Insira um valor para ser sacado: "))

                saldo, mensagem_extrato, saques_realizados = sacar(saldo=saldo, valor_para_saque=valor_para_saque, mensagem_extrato=mensagem_extrato, limite_saque=LIMITE_SAQUE, saques_realizados=saques_realizados)
            
            else: 
                print("Seu limite de 3 saques diários foi alcançado! Operacao de saque finalizada")

        elif opcao == "e":
            extrato(saldo, mensagem_extrato=mensagem_extrato)

        elif opcao == "c":
            criar_usuario(lista_usuarios)

        elif opcao == "cc":
            criar_conta(lista_contas, lista_usuarios)

        elif opcao == "l":
            listar_contas(lista_contas)

        elif opcao == "q":
            print("Saindo do sistema. Volte sempre!")
            break

        else: 
            print("Insira uma opcao valida!!")

main()