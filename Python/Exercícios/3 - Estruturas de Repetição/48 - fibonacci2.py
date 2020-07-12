"""Faça um programa que some os termos de valor par da sequência de Fibonacci,
cujos valores não ultrapassem quatro milhões. """
sequencia = []
sequencia2 = []
sequencia.append(0)
sequencia.append(1)
x = 1
m = 1
while m < 4000000:
    sequencia.append(m)
    m += sequencia[x]
    x += 1

for x in sequencia: 
    if x % 2 == 0:
        sequencia2.append(x)

print(f"Soma dos valores pares da sequência: {sum(sequencia2)} \nSequencia dos pares de fibonacci: {sequencia2}")