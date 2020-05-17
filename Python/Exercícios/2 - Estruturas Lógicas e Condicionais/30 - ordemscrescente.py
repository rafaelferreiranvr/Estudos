#Faça um programa que receba uma quantidade qualquer de números e mostre-os em ordem crescente. 
iteracoes = int(input("Quantos números você vai digitar?"))
indice = iteracoes - 1
a = []
a.append(int(input("Digite um número: "))) 
for x in range(iteracoes - 1):
    a.append(int(input("Digite outro número: ")))

b = []
for x in range(iteracoes):
    b.append(0)

for x in range(indice):
        if a[x] > b[indice]:
            b[indice] = a[x]
            
for y in range(iteracoes):
    for x in range(iteracoes):
        if a[x] > b[indice-1-y] and a[x] < b[indice-y]:
            b[indice-1-y] = a[x]

print(f"Números em ordem crescente: {b}")




