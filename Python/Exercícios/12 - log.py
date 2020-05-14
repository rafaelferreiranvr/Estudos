'''Ler um número inteiro. Se o número lido for negativo, escreva a mensagem Número inválido. 
Se o número for positivo, calcular o logaritmo deste numero. '''
from math import log as log 
num = float(input("Digite um número: "))
base = float(input("Digite a base do log: "))
loga = log(num, base)
print(f"Logarítmo de {num} na base {base}: {loga}")