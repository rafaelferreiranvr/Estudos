"""Faca uma funcão e um programa de teste para o cálculo do volume de uma esfera. 
Sendo que o raio é passado por parâmetro. 
"""
n = float(input("Digite o raio da esfera: "))
def volume(x):
    return ((4/3) * 3.14159 * (x**3))
print(f"Volume da esfera: {volume(n)}")