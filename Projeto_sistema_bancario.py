def menu():
    menu = """
=================== MENU =================== 
      
      [1] - Depósito
      [2] - Saque
      [3] - Extrato
      [4] - Criar usuário
      [5] - Criar conta
      [6] - Listar contas
      [7] - Sair 
        
      
============================================      
      
"""
    return (input(menu))



def depositar(saldo, valor, extrato,/):

    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("Valor depositado!")

    else:
        print("Operação falhou! O valor informado é inválido.") 
    
    return saldo, extrato



def sacar(*,saldo, valor, extrato, limite, numero_saques, limite_saques):

    if valor <= 0:
        print("Operação falhou! Valor inválido.")

    elif valor > saldo:
        print("Operação falhou! Saldo insuficiente.")

    elif valor > limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif numero_saques >= limite_saques:
        print("Operação falhou! Limite de saques diário atingido.")

    else:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("Saque realizado!")

    return saldo, extrato, numero_saques


def exibir_extrato(saldo, /, *, extrato):

    if extrato == "":
        print("Não foram realizadas movimentações")

    else:
        extrato += f"Saldo: R$ {saldo:.2f}\n"
        print(extrato)
  

def criar_usuario(usuarios):
    cpf = input("Informe seu CPF (somente os números) : ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Já existe usuário com esse CPF!")
        return
    nome = input("Digite seu nome : ")
    data_nascimento =  input("Informe sua data de nascimento (dd-mm-aaaa) : ")
    endereco = input("Informe seu endereço (logradouro - bairro - cidade/sigla estado)")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})    


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe seu CPF (somente os números) : ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nConta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\nUsuário não encontrado, fluxo de criação de conta encerrado! ")



def listar_contas(contas):
    for conta in contas:
        linha = f"""
        Agência:\t{conta['agencia']}
        C/C:\t\t{conta['numero_conta']}
        Titular:\t{conta['usuario']['nome']}
        """
        print(linha)    
  

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "1":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "2":
            valor = float(input("Informe o valor do saque: ")) 

            saldo, extrato, numero_saques = sacar(saldo = saldo, valor = valor, extrato = extrato, limite = limite, numero_saques = numero_saques, limite_saques = LIMITE_SAQUES)

        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)   

        elif opcao == "4":
            criar_usuario(usuarios)

        elif opcao == "5":
            numero_conta = len(contas) + 1
            conta =  criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)     

        elif opcao == "6":
            listar_contas(contas)

        elif opcao == "7":
            print("Obrigado por usar nosso sistema bancário !! ")
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")   

main() 