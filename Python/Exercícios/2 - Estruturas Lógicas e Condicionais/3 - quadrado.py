"""Leia um numero real. Se o número for positivo imprima a raiz quadrada. 
Do contrário. imprima o numero ao quadrado. 
"""
num = float(input("Digite um número: "))
if num > 0:
    print(f"Raíz do número: {num**(1/2)}")
else: 
    print(f"Número ao quadrado: {num**2}")