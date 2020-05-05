n = int(input("Digite um número de 0 a 9999: "))
if n < 0 or n  > 9999:
    n = int(input("Digite um número de 0 a 9999: "))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print("Unidade: ",u)
print("Dezena: ",d)
print("Centena: ",c)
print("Milhar: ",m)
