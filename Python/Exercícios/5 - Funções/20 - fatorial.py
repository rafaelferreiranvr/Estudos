""" Faça uma função que receba um número inteiro positivo
N e calcule seu fatorial."""

n = int(input("Digite um número: "))


def fatorial(x):
    fat = x
    for y in range(1, x):
        fat *= (x - y)
    if x == 0:
        fat = 1
    return fat


print(f"Fatorial de {n}: {fatorial(n)}")
