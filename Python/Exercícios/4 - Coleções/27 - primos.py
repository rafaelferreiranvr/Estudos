"""Leia 10 números inteiros e armazene em um vetor. 
Em seguida escreva os elementos que são primos e suas respectivas posições no vetor. """
a = []
for x in range(10):
    a.append(int(input("Digite um número: ")))
i = 0
pindices = []
for x in a:
    i += 1
    divisores = []
    for y in range(1, i + 1):
        if x % y == 0:
            divisores.append(y)
    if len(divisores) == 2:
        pindices.append(f"Primo: {x}, Posição no vetor: {i}")

for x in pindices:
    print(x)
            
