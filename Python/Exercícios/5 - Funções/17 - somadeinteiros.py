"""Faça uma função que receba dois números inteiros positivos por parâmetro
e retorne a soma dos números inteiros existentes entre eles."""
a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))


def soma(x, y):
    soma = 0
    for z in range((x + 1), y):
        soma += z
    return soma


print(f"Soma dos números inteiros entre {a} e {b}: {soma(a, b)}")
