"""Faça um programa que leia dois vetores de 10 elementos. 
Crie um vetor que seja a união entre os 2 vetores anteriores, ou seja, que contém os números dos dois vetores. 
Não deve conter números repetidos. 
"""
a = set()
b = set()
for x in range(10):
    a.add(int(input("Digite um número para o vetor A: ")))
for x in range(10):
    b.add(int(input("Digite um número para o vetor B: ")))

print(f"União entre os dois vetores: {a.union(b)}")