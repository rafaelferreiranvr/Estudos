"""Faça um programa que simula o lançamento de dois dados, d1 e d2, n vezes 
e tem como salda o número de cada dado e a relação entre eles (<, >, =) 
de cada lançamento. """
from random import randint as random
l = int(input("Quantos lançamentos você quer? "))
mensagens = []
for x in range(l):
    a = random(1, 6)
    b = random(1, 6)

    possibilidades = {
        a > b : ">",
        a < b : "<",
        a == b : "="
    }

    mensagens.append(f"{a} {possibilidades[True]} {b}")

print("Lançamentos feitos: ")
for x in mensagens:
    print(x)
