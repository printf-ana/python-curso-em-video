
salario = float(input("Digite o salário R$"))
if salario > 1250:
    salario = salario + ((10/100) * salario)
    print("O salário com 10% de aumento vira R${}".format(salario))
else:
    salario = salario + ((15/100) * salario)
    print("O salário com 15% de aumento vira R${}".format(salario))
