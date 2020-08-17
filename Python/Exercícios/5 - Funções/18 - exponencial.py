"""Faça uma função que receba por parâmetro dois valores X e Z
Calcule e retorne o resultado de X^Z para o programa principal
Atenção: não utilize nenhuma função pronta de exponenciação
"""
x = int(input("Digite um número: "))
z = int(input("Digite outro número: "))


def exponencial(a, b):
    exp = a
    for y in range(b-1):
        exp *= a
    return exp


print(f"{x} elevado a {z}: {exponencial(x, z)}")
