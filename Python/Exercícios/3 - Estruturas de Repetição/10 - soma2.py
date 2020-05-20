# Faça um programa que calcule e mostre a soma dos N primeiros números pares.
n = int(input("Digite um número: "))
soma = 0
for x in range(0, n):
    soma += 2*x
print(f"Soma dos {n} primeiros números pares: {soma}")
