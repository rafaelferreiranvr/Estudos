"""Escreva um programa que leia um número inteiro positivo n e em seguida imprima n linhas do chamado Triangulo de Floyd. 
Para n = 6, temos: 
1 
2 3 
4 5 6
7 8 9 10
11 12 13 14 15
16 17 18 19 20 21
"""
n = int(input("Digite um valor inteiro: "))
x = 0
m = 1
while x != n:
    x += 1
    for y in range(x):
        print(m, end=" ")
        m += 1
    print()


   