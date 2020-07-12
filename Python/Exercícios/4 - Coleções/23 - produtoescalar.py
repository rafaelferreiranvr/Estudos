"""Ler dois conjuntos de números reais 
armazenando-os em vetores e calcular o produto escalar entre eles. 
Os conjuntos tem 5 elementos cada. Imprimir os dois conjuntos e o produto escalar, 
sendo que o produto escalar é dado por: x1*y1 + x2*y2 + xn*yn"""
a = []
b = []
produto = 0
for x in range(5):
    a.append(int(input("Digite um número para o vetor A: ")))
for x in range(5):
    b.append(int(input("Digite um número para o vetor B: ")))
for x in range(5):
    produto += a[x]*b[x]
print(f"Produto escalar: {produto}")