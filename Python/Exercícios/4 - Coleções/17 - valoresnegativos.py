#Leia um vetor de 10 posições e atribua valor 0 para todos os elementos que possuírem valores negativos. 
a = []
for x in range(0, 10):
    a.append(int(input("Digite um número: ")))
    if a[x] < 0:
        a[x] = 0
print(a)