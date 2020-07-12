"""Faça um programa que leia um vetor de 10 números. 
Leia um número x.
Conte os múltiplos de um número inteiro x num vetor e mostre-os na tela. """
a = []
b = []
for x in range(10):
    a.append(int(input("Digite um elemento do vetor: ")))
n = int(input("Digite um número para pesquisar os multiplos: "))
for x in a:
    if x % n == 0:
        b.append(x)
print(f"Múltiplos de {n} digitados: {b}")