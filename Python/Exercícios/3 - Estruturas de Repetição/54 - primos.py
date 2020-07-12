"""Faça um programa que receba um número inteiro maior do que 1, 
e verifique se o número fornecido é primo ou não. 
"""
n = int(input("Digite um número: "))
divisores = []
for x in range(1, n+1):
    if n % x == 0:
        divisores.append(x)
if len(divisores) == 2:
    print("Esse número é primo. ")
else:
    print("Esse número não é primo.")