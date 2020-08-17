"""Faça uma função que receba uma temperatura em graus Celsius e
retorne-a convertida em graus Fahrenheit.
A fórmula de conversão é: F = C * (9.0/5.0) + 32.0, sendo F
a temperatura em Fahrenheit e C a temperatura em Celsius.
"""
n = float(input("Digite um valor de temperatura em Celsius: "))


def conversor(c):
    f = (9*c/5) + 32
    return f


print(f"Temperatura em Fahrenheit: {conversor(n)}")
