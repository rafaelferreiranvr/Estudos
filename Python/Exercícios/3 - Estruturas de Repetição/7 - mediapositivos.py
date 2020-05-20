#Faça um programa que leia N inteiros positivos. ignorando não positivos. e imprima sua média.
n = int(input("Quantos valores você vai digitar?(Somente positivos serão considerados) "))
soma = 0 
z = 0
for x in range(n):
    m = int(input("Digite um número: "))
    if m > 0:
        soma += m
        z += 1
if z > 0:
    media = soma/z
    print(f"Média dos valores: {media:.1f}")
else:
    print("Nenhum valor positivo foi digitado, sem média.")