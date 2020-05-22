"""Faça um programa que leia um número inteiro positivo N e 
imprima todos os números naturais de 0 até N em ordem decrescente. """
n = int(input("Digite um número: "))
print("Sequência: ")
for x in range(n, -1, -1):
    if x == (1):
        print(x, end=" e ")
    elif x == (0):
        print(x)
    else:
        print(x, end=", ")