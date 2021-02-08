import random

n = 1 

while n != 2:
    print("---MENU---\n"
    +"1-Gerar um numero\n"
    +"2-Finalizar programa")
    n = int(input("Informe a opcao desejada:"))
    if n == 1:
        dado = random.randint(1,6)
        print(dado)
    elif n == 2:
        print("Programa Finalizado!")
        exit(0)
    else:
        print("Numero invalido!")
        