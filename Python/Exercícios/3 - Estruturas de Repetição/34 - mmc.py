"""Faça um programa que calcule o menor número divisível por 
cada um dos números de 1 a N? Ex: 2520 é o menor 
número que pode ser dividido por cada um dos números de 1 a 10, 
sem sobrar resto. """

n = int(input("Digite um número: "))
sequencia = []
condicoes = []
for x in range(1, n+1):
    sequencia.append(x)

maior = max(sequencia)

while True:   
    condicoes.clear() 
    for x in sequencia: 
        if maior % x == 0:
            condicoes.append(True)
        else:
            condicoes.append(False)
    if all(condicoes):
        break
    else:
        maior += 1


print(f"MMC dos números de 1 a {n}: {maior}")    
    
            

