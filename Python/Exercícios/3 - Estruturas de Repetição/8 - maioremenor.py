#Escreva um programa que leia n números e escreva o menor valor lido e o maior valor lido.
n = int(input("Quantos números você vai digitar? "))
a = []
M = 0
m = 0

for x in range(n):
    a.append(int(input("Digite um número: "))) 

for x in range(n):
    if a[x] >= M:
        M = a[x]
        m = a[x]
    
for x in range(x):
    if a[x] <= m:
        m = a[x]

print(F"Maior número: {M}, menor número: {m}")