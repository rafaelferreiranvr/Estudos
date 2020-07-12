#Faça um programa que calcule a soma de todos os números primos abaixo de vinte mil. 
i = 1
soma = 0

while i != 20000:
    i += 1
    
    divisores = []
    for x in range(1, i+1):
        if i % x == 0:
            divisores.append(x)
    
    if len(divisores) == 2:
        soma += i
        print(i)

print(f"Soma dos números primos menores que 2 mil: {soma}")