"""Escreva um programa para calcular o valor da série, para N termos.
S = O + 1/2! + 2/4! + 3/6! + ... 
"""


def fatorial(a):
    f = a
    for x in range(1, a):
        f *= (a-x)
    return f


n = int(input("Digite um valor: "))
s = 0
for x in range(1, n+1):
    m = fatorial(2*x)
    s += x/m
print(f"Valor de S = {s}")
