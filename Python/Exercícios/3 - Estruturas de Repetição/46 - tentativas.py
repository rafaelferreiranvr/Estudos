"""Faça um programa que gera um número aleatório de 1 a 1000. 
O usuário deve tentar acertar qual o número foi gerado, 
a cada tentativa o programa deverá informar se o chute é menor ou maior que o número gerado. 
O programa acaba quando o usuário acerta o número gerado. 
O programa deve informar em quantas tentativas o número foi descoberto. """
from random import randint as random
n = random(1, 1000)
m = 0
palpites = 0
while m != n:
    m = int(input("Digite um palpite: "))
    if m > n:
        print("O número digitado é maior que o correto.") 
    elif m < n:
        print("O número digitado é menor do que o correto.")
    else:
        print("O número digitado é o correto.")
    palpites += 1
print(f"Palpites necessários: {palpites}")