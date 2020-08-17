"""Elabore uma função que receba três notas de um aluno
como parâmetros e uma letra.
Se a letra for A, a função deverá calcular a média aritmética
das notas do aluno: se for P, deverá calcular a média ponderada, ,
com pesos 5, 3 e 2. """
a = float(input("Digite a primeira nota: "))
b = float(input("Digite a segunda nota: "))
c = float(input("Digite a terceira nota: "))
letra = input("Digite 'A' para média aritmética ou 'P' para média ponderada: ")


def media(x, y, z, t):
    if t == "A":
        m = (x + y + z)/3
    elif t == "P":
        m = (5*x + 3*y + z*2)/10
    return m


print(f"Média das notas: {media(a, b, c, letra)}")
