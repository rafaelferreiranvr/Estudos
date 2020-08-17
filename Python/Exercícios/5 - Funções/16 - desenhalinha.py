"""Faça uma função chamada DesenhaLinha. Ele deve desenhar uma linha na tela
usando vários símbolos de igual (Ex: ======).
A função recebe por parâmetro quantos sinais de igual serão mostrados.
"""
n = int(input("Digite quantos sinais de igual a linha deve ter: "))


def DesenhaLinha(i):
    for z in range(i):
        print("=", end="")


DesenhaLinha(n)
