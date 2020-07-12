"""Faça um programa que receba do usuário dois vetores, A e B, com 10 números inteiros cada.
Crie um novo vetor denominado C calculando C = A - B. Mostre na tela os dados do vetor C."""
a = []
b = []
c = []
for x in range(10):
    a.append(int(input("Digite um valor para o vetor A: ")))
for x in range(10):
    b.append(int(input("Digite um valor para o vetor B: ")))
for x in range(10):
    c.append(a[x] - b[x]) 
print(f"Vetor C: {c}")
