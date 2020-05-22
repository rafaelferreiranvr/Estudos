# Escreva um programa que leia um número inteiro e calcule a soma de todos os divisores desse número, com exceção dele próprio.
# Ex: a soma dos divisores do número 66 é 1 + 2 + 3 + 6 + 11 + 22 + 33 = 78
n = int(input("Digite um número: "))
soma = 0
for x in range(1, n+1):
    if n % x == 0 and x != n:
        soma += x
print(f"Soma dos divisores excluindo ele próprio: {soma}")
