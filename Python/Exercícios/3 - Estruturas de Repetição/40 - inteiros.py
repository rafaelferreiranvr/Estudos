"""Elabore um programa que faça leitura de vários números inteiros, 
até que se digite um número negativo. 
O programa tem que retornar o maior e o menor número lido. 
"""
n = 0
lista = []
while n >= 0:
    n = int(input("Digite um número: "))
    lista.append(n)

print(f"Maior número: {max(lista)}, Menor Número: {min(lista)}")