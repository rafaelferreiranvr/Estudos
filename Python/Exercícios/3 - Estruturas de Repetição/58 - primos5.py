#Faça um programa que some os números primos existentes entre a e b, onde a e b são números informados pelo usuário. 
i = int(input("Digite o inicio do intervalo: "))
n = int(input("Digite o final do intervalo: "))
l = i
i = 0
soma = 0

while i != n:
    i += 1
    
    divisores = []
    for x in range(1, i+1):
        if i % x == 0:
            divisores.append(x)

    if len(divisores) == 2:
        soma += i


print(f"Soma dos primos entre {l} e {n}: {soma}")