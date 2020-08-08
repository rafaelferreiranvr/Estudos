"""Faca uma função para verificar se um número é positivo ou negativo. 
Sendo que o valor de retorno será 1 se positivo, -1 se negativo e 0 se for igual a 0. 
"""
n = int(input("Digite um número: "))
def posneg(x):
    if x < 0:
        return f"Código: -1 \nNúmero Negativo"
    elif x == 0:
        return f"Código: 0 \nNúmero 0"
    else:
        return f"Código 1 \nNúmero positivo"
print(posneg(n))