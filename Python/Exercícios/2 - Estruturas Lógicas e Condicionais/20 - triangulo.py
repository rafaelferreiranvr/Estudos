"""Dados três valores, A, B, C, verificar se eles podem ser valores dos lados de um triângulo e, 
se forem, se é um triângulo escaleno, equilátero ou isóscele, considerando os seguintes conceitos: 
O comprimento de cada lado de um triângulo é menor do que a soma dos outros dois lados. 
Chama-se equilátero o triângulo que tem três lados iguais. 
Denominam-se isósceles o triângulo que tem o comprimento de dois lados iguais. 
Recebe o nome de escaleno o triângulo que tem os três lados diferentes."""
a = float(input("Lado A: "))
b = float(input("Lado B: "))
c = float(input("Lado C: "))
if a < (b + c) and b < (a + c) and c < (a + b):
    if a == b == c:
        print("Tipo de triângulo: Equilátero.")
    elif a != b != c:
        print("Tipo de triângulo: Escaleno")
    else:
        print("Tipo de triângulo: Isósceles. ")
else:
    print("Triângulo não existe.")
