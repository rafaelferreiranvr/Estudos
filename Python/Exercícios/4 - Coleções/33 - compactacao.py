"""Faça um programa que leia um vetor de 15 posições e o compacte, ou seja, elimine as posições com valor zero. 
Para isso, todos os elementos à frente do valor zero, devem ser movidos uma posição para trás no vetor. 
"""
a = []
for x in range(15):
    a.append(int(input("Digite um número para o vetor A: ")))

while 0 in a:
    n = a.index(0)
    for x in range(len(a)):
        if x >= n:
            try:
                a[x] = a[x+1]
            except IndexError:
                a.pop()
print(f"Vetor compactado: {a}")
            