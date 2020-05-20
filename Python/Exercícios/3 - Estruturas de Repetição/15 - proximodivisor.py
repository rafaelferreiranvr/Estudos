# Faca um algoritmo que encontre o primeiro múltiplo de 11, 13 ou 17 após um número dado.
n = int(input("Digite um número: "))
if n % 11 == 0 or n % 13 == 0 or n % 17 == 0:
    n += 1

while (n % 11 != 0) and (n % 13 != 0) and (n % 17 != 0):
    n += 1

print(f"Número encontrado: {n}")
