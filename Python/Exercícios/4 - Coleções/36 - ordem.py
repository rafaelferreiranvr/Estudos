"""Leia um vetor com 10 números reais, ordene os elementos deste vetor, 
e no final escreva os elementos do vetor ordenado. """
a = []
for x in range(10):
    a.append(int(input("Digite um número: ")))

print(f"Vetor ordenado: {sorted(a)}")