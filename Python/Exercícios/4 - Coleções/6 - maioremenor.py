"""Faça um programa que receba do usuário um vetor com 10 posições. 
Em seguida deverá ser impresso o maior e o menor elemento do vetor. 
"""
a = []
a.append(int(input("Digite um número: ")))

for x in range(0, 10):
    a.append(int(input("Digite um outro número: ")))
    
print(f"Valor mínimo: {min(a)}, Valor máximo: {max(a)}")