
menu = "\nBANCO\n Digite o numero para:\n 1. Depositar\n 2. Sacar\n 3. Ver extrato\n 4. Sair\n"

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

# deposito: 
# depositos devem ser armazenados em uma variavel e exibidos na operacao de extrato
    if opcao == '1':
        deposito = float(input("Digite o valor do deposito: "))

#fazer try catch para nao aceitar string, somente numeros
        #try:
            #deposito = float(input("Digite o valor do depósito: "))
        #except ValueError:
            #print("Inválido, insira um número.")

        if deposito > 0:
            saldo += deposito
            extrato += f"Depósito: R$ {deposito}\n"
            #extrato += f"Depósito: R$ {deposito:.2f}\n"

        if(deposito<0):
            print("São aceitos somente valores positivos. ")

        print("saldo: ", saldo)
        print("extrato: ", extrato)

# saque: 
# tres saques diarios com limite maximo de 500 por saque
# se não tiver saldo, mostrar mensagem. 
# todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato
    elif opcao == '2':
        saque = float(input("Digite o valor do saque: "))
        saldo = limite - saque

        if(saque>limite):
            print(f"Limite de {limite} atingido. Digite um valor menor.")
        print("saque")

# extrato:
# listar todos os depósitos e saques realizados na conta
# no final, deve ser listado o saldo atual da conta
# se extrato estiver em branco, aparecer (não foram realizadas movimentações)
# valores devem ser exibidos com R$
    elif opcao == '3':
        print("===== EXTRATO =====\n", extrato)

    elif opcao == '4':
        break

    else:
        print("Operação inválida, tente novamente.")