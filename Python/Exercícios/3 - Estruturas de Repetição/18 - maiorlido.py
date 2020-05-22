# Escreva um algoritmo que leia certa quantidade de números e imprima o maior deles e quantas vezes o maior número foi lido.
# A quantidade de números a serem lidos deve ser fornecida pelo usuário.
n = int(input("Quantos números serão digitados? "))
a = []
maior = 0
q = 0
for x in range(n):
    a.append(int(input("Digite um número: ")))
    if a[x] > maior:
        maior = a[x]

for x in range(n):
    if a[x] == maior:
        q += 1

print(f"O maior número digitado foi {maior} e foi digitado {q} vezes.")
