"""Sejam a e b os  catetos de um triângulo, onde a hipotenusa é obtida
pela equação:
hipotenusa^2 = a^2 + b^2.
Faça uma função que receba os valores de a e b e calcule
o valor da hipotenusa através da equação.
"""

a = float(input("Digite um dos catetos do triângulo retângulo: "))
b = float(input("Digite o outro cateto do triângulo retângulo: "))


def pitagoras(x, y):
    h = (x**2 + y**2)**(1/2)
    return h


print(f"Hipotenusa: {pitagoras(a, b)}")
