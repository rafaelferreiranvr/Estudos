"""Escreva um programa que leia números inteiros no intervalo [0, 50] e os armazene em um vetor com 10 posições. 
Preencha um segundo vetor apenas com os números impares do primeiro vetor. 
Imprima os dois vetores, 2 elementos por linha. 
"""
a = []
b = []
for x in range(10):
    n = int(input("Digite um número entre 0 e 50: "))
    if n > 50 or n < 0:
        raise Exception("Somente números entre 0 e 50 são permitidos.")
    a.append(n)

for x in a:
    if x % 2 != 0:
        b.append(x)

print("Primeiro vetor: ")
for x in range(0, len(a), 2):
    try:
        print(a[x], end=" ")
        print(a[x+1])
    except:
        print(a[x])

print("Vetor apenas de ímpares: ")
for x in range(0, len(b), 2):
    try:
        print(b[x], end=" ")
        print(b[x+1])
    except:
        print(b[x])
    

