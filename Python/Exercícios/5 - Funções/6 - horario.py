"""Faca uma função que receba 3 números inteiros como parâmetro,
representando horas, minutos e segundos, e os converta em segundos.
"""
n = input("Digite um horário no formato H:MM:SS ")


def segundos(x):
    m = n.split(":")
    s = int(m[0]) * 3600
    s += int(m[1]) * 60
    s += int(m[2])
    return s


print(f"Horário digitado em segundos: {segundos(n)}")
