"""Faça um programa que leia um número inteiro positivo N e calcule a soma dos N primeiros numeros naturais."""
n = int(input("Digite um número: "))
soma = 0
for x in range(n+1):
    soma += x
print(f"Soma dos {n} primeiros números naturais: {soma}")
