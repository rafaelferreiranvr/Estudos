"""Faça um programa que leia um número inteiro positivo N e 
imprima todos os números impares de 0 até N em ordem decrescente. """
n = int(input("Digite um número: "))
print("Sequência: ")
if n%2==0:
    for x in range(n-1, 0, -2):
        if x == 1:
            print(x)
            break
        if x == 3:
            print(x, end=" e ")
        else:
            print(x, end=", ")
else:
    for x in range(n, 0, -2):
        if x == 1:
            print(x)
            break
        if x == 3:
            print(x, end=" e ")
        else:
            print(x, end=", ")
