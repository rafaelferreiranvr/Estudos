#Faça um programa que peça ao usuário para digitar n valores e some-os. 
n = int(input("Quantos valores você vai digitar? "))
soma = 0 
for x in range(n):
    m = int(input("Digite um número: "))
    soma += m
print(f"Soma dos números: {soma}")