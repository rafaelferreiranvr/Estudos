"""Faça um programa que calcule a área de um triângulo,
cuja base e altura são fornecidas pelo usuário. 
Esse programa não pode permitir a entrada de dados inválidos, ou seja,
medidas menores ou iguais a 0. 
"""
base = float(input("Digite a base do triângulo: "))
altura = float(input("Digite a altura do triângulo: "))
if base <= 0 or altura <= 0:
    raise TypeError("Não são aceitas medidas menores que 0.")

area = base*altura/2
print(f"Altura: {area}")
