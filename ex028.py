from random import randint
from time import sleep
computador = randint(0,5) #Faz o computador pensar num número
print("Pense em um número de 0 a 5.")

jogador = int(input("Que número você pensou? "))

if jogador == computador:
    print("Você acertou!")
else:
    print("Errou, o número era {}, não {}".format(computador,jogador)) 
