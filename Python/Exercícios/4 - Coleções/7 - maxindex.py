"""Escreva um programa que leia 10 números inteiros e os armazene em um vetor. 
Imprima o vetor, o maior elemento e a posição que ele se encontra. 
"""
a = []
a.append(int(input("Digite um número: ")))

for x in range(0, 10):
    a.append(int(input("Digite um outro número: ")))
    
print(f"Valor máximo: {max(a)}, Posição dele: {a.index(max(a))}")
