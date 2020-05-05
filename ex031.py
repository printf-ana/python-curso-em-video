distancia = float(input("Digite a distância de uma viagem: "))
valor = 0
if distancia <= 200:
    valor = distancia * 0.50
    print("O valor da passagem será de R${:.2f}".format(valor))
else:
    valor = distancia * 0.45
    print("O valor da passagem será de R${:.2f}".format(valor))
