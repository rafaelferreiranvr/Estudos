#Faça um programa que leia N inteiros e imprima sua média. 
n = int(input("Quantos valores você vai digitar? "))
soma = 0 
for x in range(n):
    m = int(input("Digite um número: "))
    soma += m
media = soma/n
print(f"Média dos valores: {media:.1f}")
