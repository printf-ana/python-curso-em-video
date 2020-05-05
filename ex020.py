import random
a1 = input("Digite o nome do primeiro aluno: ")
a2 = input("Digite o nome do segundo aluno: ")
a3 = input("Digite o nome do terceiro aluno: ")
a4 = input("Digite o nome do quarto aluno: ")
lista = [a1,a2,a3,a4]
random.shuffle(lista)
print("A ordem de escolhidos foi:",lista)



if escolhido == "Pedra" and escolha == "papel" or escolha == "Papel":
        print(nome,escolha,"X",escolhido,"Computador")
        print("Você venceu!\n")
    elif escolhido == "Pedra" and escolha == "tesoura" or escolha == "Tesoura":
        print(nome,escolha,"X",escolhido,"Computador")
        print("Você perdeu!\n")
    elif escolhido == "Papel" and escolha == "tesoura" or escolha == "Tesoura":
        print(nome,escolha,"X",escolhido,"Computador")
        print("Você ganhou!\n")
    elif escolhido == "Papel" and escolha == "pedra" or escolha == "Pedra":
        print(nome,escolha,"X",escolhido,"Computador")
        print("Você perdeu!\n")
    elif escolhido == "Tesoura" and escolha == "papel" or escolha == "Papel":
        print(nome,escolha,"X",escolhido,"Computador")
        print("Você perdeu!\n")
    elif escolhido == "Tesoura" and escolha == "pedra" or escolha == "Pedra":
        print(nome,escolha,"X",escolhido,"Computador")
        print("Você ganhou!\n")
