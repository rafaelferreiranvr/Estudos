"""Faça um programa que receba 6 números inteiros e mostre: 
Os números pares digitados 
A soma dos números pares digitados
Os números impares digitados
A quantidade de números ímpares digitados 
"""
v = []
v1 = []
v2 = []
for x in range(10):
    v.append(int(input("Digite um número: ")))

for x in v:
    if x % 2 == 0:
        v2.append(x)
    else:
        v1.append(x)
print(f"Pares digitados: {v2} \nSoma dos pares digitados: {sum(v2)} \nNúmeros ímpares: {v1} \nQuantidade de ímpares: {len(v1)}")