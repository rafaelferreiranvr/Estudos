"""Faça um programa que leia um número indeterminado de idades de indivíduos (pare quando for informada a idade 0), 
e calcule a idade média desse grupo. 
"""
n = 1
soma = 0
quantidade = 0
while n != 0:
    n = int(input("Digite uma idade: "))
    soma += n
    quantidade += 1
print(f"Média das idades: {soma/quantidade}")
    