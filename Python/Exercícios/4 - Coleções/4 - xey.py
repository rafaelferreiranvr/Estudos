"""Faça um programa que leia um vetor de 8 posições e, em seguida, leia também dois va-
lores X e Y quaisquer correspondentes a duas posições no vetor.
Ao final seu programa deverá escrever a soma dos valores encontrados nas respectivas posições X e Y."""
from random import choice as choice
a = []
x = 0
y = 0
a.append(int(input("Digite um número: ")))

for x in range(0, 8):
    a.append(int(input("Digite um outro número: ")))

while x == y:
    x = choice(a)
    y = choice(a)

print(x, y)