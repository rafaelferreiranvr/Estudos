"""Escreva um programa que receba como entrada o valor do saque realizado 
pelo cliente de um banco e retorne quantas notas de cada valor serão necessárias
para atender ao saque com a menor quantidade de notas possível. 
Serão utilizadas notas de 100, 50, 20, 10, 5, 2 e 1 real. """
saque = int(input("Digite o valor do saque: "))
temp = 0
n1 = 0
n2 = 0
n5 = 0
n10 = 0
n20 = 0
n50 = 0
n100 = 0

while temp != saque:
    if (temp + 100) <= saque:
        temp += 100
        n100 += 1
    elif (temp + 50) <= saque:
        temp += 50
        n50 += 50
    elif (temp + 20) <= saque:
        temp += 20
        n20 += 1
    elif (temp + 10) <= saque:
        temp += 10
        n10 += 1 
    elif (temp + 5) <= saque:
        temp += 5 
        n5 += 1
    elif (temp + 1) <= saque:
        temp += 1 
        n5 += 1

for x in range(6):
    if n100 != 0:
        print(f"Número de notas de 100 necessárias: {n100}")
        n100 = 0
    elif n50 != 0:
        print(f"Número de notas de 50 necessárias: {n50}")
        n50 = 0
    elif n20 != 0:
        print(f"Número de notas de 20 necessárias: {n20}")
        n20 = 0
    elif n10 != 0:
        print(f"Número de notas de 10 necessárias: {n10}")
        n10 = 0
    elif n5 != 0:
        print(f"Número de notas de 5 necessárias: {n5}")
        n5 = 0
    elif n1 != 0:
        print(f"Número de notas de 1 necessárias: {n1}")
        n1 = 0


