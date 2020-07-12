"""Escreva um programa que leia um inteiro não negativo n e imprima a soma dos n 
primeiros números primos. 
"""
n = int(input("Digite um número: "))
i = 1
soma = 0
q = 0

while q != n:
    i += 1
    
    divisores = []
    for x in range(1, i+1):
        if i % x == 0:
            divisores.append(x)

    if len(divisores) == 2:
        q += 1
        soma += i

print(f"Soma dos {n} números primos: {soma}")