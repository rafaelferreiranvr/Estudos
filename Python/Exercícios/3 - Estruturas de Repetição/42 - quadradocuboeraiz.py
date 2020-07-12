"""Faça um programa que leia um conjunto não determinado de valores. um de cada vez, 
e escreva para cada um dos valores lidos. o quadrado. o cubo e a raiz quadrada. 
Finalize a entrada de dados com um valor negativo ou zero. """
n = 1
while n > 0:
    n = int(input("Digite um número: "))
    print(f"Raíz desse número: {n**(1/2)} \nQuadrado do número: {n**2} \nCubo do Número: {n**3}")
