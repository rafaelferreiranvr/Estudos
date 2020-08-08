"""Faca uma funcão para verificar se um numero é um quadrado perfeito. 
Um quadrado perfeito e um numero inteiro não negativo que pode ser expresso como o quadrado de outro numero inteiro. 
Ex: 1, 4, 9... 
"""
n = int(input("Digite um número inteiro: "))
def quadrado(x):
    if x**(1/2) % 1 == 0:
        return "Esse número é um quadrado perfeito."
    else:
        return "Esse número não é um quadrado perfeito."
print(quadrado(n))