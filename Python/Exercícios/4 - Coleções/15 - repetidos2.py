"""Leia um vetor com 20 números inteiros. Escreva os elementos do vetor eliminando 
elementos repetidos. """
a = []
b = {}
q = 0
for x in range(20):
    a.append(int(input("Digite um número: ")))

print(f"Velor antes: {a}")
for x in a:
    for y in a:
        if x == y:
            q += 1
    b.update({x : q})
    q = 0

for x in b:
    if b[x] > 1:
        for y in range(b[x]):
            a.remove(x)
        
print(f"Vetor depois: {a}")
