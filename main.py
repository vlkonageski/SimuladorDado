import random

n = 1 

while n != 2:
    print("---MENU---\n"
    +"1-Jogar Dado\n"
    +"2-Finalizar programa")
    n = int(input("Informe a opcao desejada:"))
    if n == 1:
        print("---Selecione o Dado que deseja rolar---\n"
        +"1-D4\n"
        +"2-D6\n"
        +"3-D8\n"
        +"4-D10\n"
        +"5-D12\n"
        +"6-D20")
        x = int(input("Informe a opcao desejada:"))
        if x == 1:
            dado = random.randint(1,4)
            print(dado)
        elif x == 2:
            dado = random.randint(1,6)
            print(dado)
        elif x == 3:
            dado = random.randint(1,8)
            print(dado)
        elif x == 4:
            dado = random.randint(1,10)
            print(dado)
        elif x == 5:
            dado = random.randint(1,12)
            print(dado)
        elif x == 6:
            dado = random.randint(1,20)
            print(dado)
        else:
            print("Opcao invalida!")
    elif n == 2:
        print("Programa Finalizado!")
        exit(0)
    else:
        print("Numero invalido!")
        