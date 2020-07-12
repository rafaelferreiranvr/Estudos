#Faça um programa que conte quantos números primos existem entre a e b, onde a e b e são números informados pelo usuário. 
i = int(input("Digite o inicio do intervalo: "))
n = int(input("Digite o final do intervalo: "))
l = i
q = 0


while i != n:
    i += 1
    
    divisores = []
    for x in range(1, i+1):
        if i % x == 0:
            divisores.append(x)
    
    if len(divisores) == 2:
        q += 1

print(f"Número de primos entre {l} e {n}: {q}")