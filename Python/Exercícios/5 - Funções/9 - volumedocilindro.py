"""Faça umam função que receba a altura e o raio de um cilindro
circular e retorne o volume do cilindro.
O volume de um cilindro circular é calculado por meio
da seguinte fórmula: V = pi * raio² * altura, onde pi = 3,141592
"""
h = float(input("Digite a altura do cilíndro: "))
r = float(input("Digite o raio do cilíndro: "))
pi = 3.141592


def volume(altura, raio):
    v = pi * (raio**2) * altura
    return v


print(f"Volume do cilíndro: {volume(h, r)}")
