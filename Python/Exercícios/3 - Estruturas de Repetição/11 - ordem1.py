"""Faça um programa que leia um número inteiro positivo N e 
imprima todos os números naturais de 0 até N em ordem crescente. """
n = int(input("Digite um número: "))
print("Sequência: ")
for x in range(n+1):
    if x == (n-1):
        print(x, end=" e ")
    elif x == (n):
        print(x)
    else:
        print(x, end=", ")