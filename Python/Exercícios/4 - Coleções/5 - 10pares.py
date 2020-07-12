#Leia um vetor de 10 posições. Contar e escrever quantos valores pares ele possui. 
A = []
pares = 0
A.append(int(input("Digite um número: ")))
for x in range(10):
    A.append(int(input("Digite um outro número: ")))
for x in A:
    if x % 2 == 0:
        pares += 1
print(f"Quantidade de pares: {pares}") 