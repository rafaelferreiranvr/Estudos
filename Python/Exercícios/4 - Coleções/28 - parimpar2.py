"""Leia 10 números inteiros e armazene em um vetor V. Crie dois novos vetores V1 e V2. 
Copie os valores ímpares de para V1 e os valores pares de V para V2. 
Note que cada um dos vetores V1 e V2 têm no máximo 10 elementos,
mas nem todos os elementos são utilizados. 
No final escreva os elementos UTILIZADOS de V1 e V2.
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
print(f"Vetor 1: {v1} \nVetor 2: {v2}")