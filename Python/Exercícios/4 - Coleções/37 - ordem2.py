"""Considere um vetor A com 11 elementos onde A1 < A2 < ... < A6 > A7 > A8 > ... > A11, 
ou seja, está ordenado em ordem crescente até o sexto elemento,
e a partir desse elemento está ordenado em ordem decrescente. 
Dado o vetor da questão anterior, proponha um algoritmo para ordenar os elementos. """
a = []
for x in range(5):
    a.append(int(input("Digite um número: ")))
a = sorted(a)
b = sorted(a, reverse=True)
b.pop(0)
a.extend(b)
print(f"Vetor ordenado: {a}")