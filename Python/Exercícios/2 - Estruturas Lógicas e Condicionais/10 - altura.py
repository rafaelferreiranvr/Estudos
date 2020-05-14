'''Faça um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu peso ideal. 
Utilizando as seguintes fórmulas (onde h corresponde à altura):
Homens: (72.7 * h) - 58 
Mulheres: (62.1* h) - 44,7'''
h = float(input("Altura(em metros): "))
sexo = input("Sexo(H ou M): ")

if sexo == "H":
    print(f"Peso ideal: {(72.7*h) - 58}")
elif sexo == "M":
    print(f"Peso ideal: {(62.1*h) - 44.7}")

