"""Faça um programa que leia um número inteiro positivo N e 
imprima todos os números impares de 0 até N em ordem crescente. """
n = int(input("Digite um número: "))
print("Sequência: ")
for x in range(1, n+1, 2):
    if n%2==0:
        if x == (n-1):
            print(x)
        elif x == (n-3):
            print(x, end=" e ")
        else:
            print(x, end=", ")
    else:
        if x == (n):
            print(x)
        elif x == (n-2):
            print(x, end=" e ")
        else:
            print(x, end=", ")