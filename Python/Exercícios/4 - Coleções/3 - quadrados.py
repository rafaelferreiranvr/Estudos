"""Ler um conjunto de números reais, armazenando-o em vetor e calcular o quadrado das componentes deste vetor, armazenando o resultado em outro vetor. 
Os conjuntos têm 10 elementos cada. Imprimir todos os conjuntos."""
a = []
a.append(int(input("Digite um número: ")))
for x in range(0, 10):
    a.append(int(input("Digite um outro número: ")))
    
b = []
for x in a:
    b.append(x**2)
        
print(a)
print(b)