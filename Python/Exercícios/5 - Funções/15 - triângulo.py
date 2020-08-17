"""Crie um programa que receba três valores (obrigatoriamente
maiores que zero).
representando as medidas dos três lados de um triângulo. Elabore funções para:
(a) Determinar se eles lados formam um triângulo, sabendo que:
• O comprimento de cada lado de um triângulo é menor do que a soma dos
outros dois lados.
(b) Determinar e mostrar o tipo de triângulo, caso as
medidas formem um triângulo.
Sendo que:
• Chama-se equilátero o triângulo que tem três lados iguais.
• Denominam-se isósceles o triângulo que tem o comprimento
de dois lados iguais.
• Recebe o nome de escaleno o triângulo que tem os três lados diferentes. """

a = float(input("Digite um lado do triângulo: "))
b = float(input("Digite um outro lado do triângulo: "))
c = float(input("Digite um outro lado do triângulo: "))

if a <= 0 or b <= 0 or c <= 0:
    raise ValueError("Só são permitidos valores maiores do que zero.")


def triangulo(x, y, z):
    condicoes = [
        x < (y + z),
        y < (x + z),
        z < (x + y)
    ]
    if all(condicoes):
        if a == b == c:
            return "Triângulo Equilátero."
        elif a != b != c:
            return "Triângulo Escaleno."
        else:
            return "Triângulo Isósceles."
    else:
        return "Triângulo Inválido."


print(triangulo(a, b, c))
