"""Faça um programa que leia dois vetores de 10 posições e calcule outro vetor contendo,
nas posições pares os valores do primeiro e nas posições impares os valores do segundo. """
a = []
for x in range(10):
    a.append(int(input("Digite um valor para o vetor A: ")))
    
b = []
for x in range(10):
    b.append(int(input("Digite um valor para o vetor B: ")))

c = []
p = 0
i = 0
x = 0
while x != 20:
    if x % 2 == 0:
        c.append(a[p])
        p += 1
    else:
        c.append(b[i])
        i += 1
    x += 1
print(c)