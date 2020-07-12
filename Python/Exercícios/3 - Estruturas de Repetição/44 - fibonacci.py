"""Leia um número positivo do usuário. então. calcule e imprima a sequência Fibonacci até o primeiro número superior ao número lido. 
Exemplo: se o usuário informou o número 30, a sequência a ser impressa será 0 1 1 2 3 5 8 13 21 34. """
n = int(input("Digite um número: "))
if n < 0:
    raise Exception("Somente números positivos são permitidos.")
sequencia = []
sequencia.append(0)
sequencia.append(1)
x = 1
m = 1
while m < n:
    sequencia.append(m)
    m += sequencia[x]
    x += 1
if n != 0:
    sequencia.append(m)
print(sequencia)