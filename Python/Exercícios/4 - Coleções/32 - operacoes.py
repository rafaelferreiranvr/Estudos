"""Leia dois vetores de inteiros a e b cada um com 5 elementos (assuma que o usuário não informa elementos repetidos). 
Calcule e mostre os vetores resultantes em cada caso abaixo: 
• Soma entre a e b: soma de cada elemento de a com o elemento da mesma posição 
em b
• Produto entre a e b: multiplicação de cada elemento de a com o elemento da mesma posição em b 
• Diferença entre a e b: todos os elementos de a que não existam em b. 
• Interseção entre a e b: apenas os elementos que aparecem nos dois vetores. 
• União entre a e b: todos os elementos de a e todos os elementos de b que não estão em a."""
a = []
b = []
for x in range(5):
    a.append(int(input("Digite um número para o vetor A: ")))
for x in range(5):
    b.append(int(input("Digite um número para o vetor B: ")))

soma = []
produto = []
for x in range(5):
    soma.append(a[x] + b[x])
    produto.append(a[x]*b[x])

a = set(a)
b = set(b)

diferenca = a.difference(b)
intersec = a.intersection(b)
uniao = a.union(b)

print(f"Soma entre A e B: {soma} \nProduto entre A e B: {produto} \nDiferença entre A e B: {diferenca} \nIntersecção entre A e B: {intersec} \nUnião entre A e B: {uniao}")



