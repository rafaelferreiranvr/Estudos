"""Faça uma prova de matemática para crianças que estão aprendendo a 
somar números inteiros menores do que 100.
Escolha números aleatórios entre 1 e 100, e mostre na tela a pergunta:
qual é a soma de a + b onde a e b são os números aleatórios.
Peça a resposta. Faça cinco perguntas ao aluno, e mostre para ele as 
perguntas e as respostas corretas, além de quantas vezes o aluno acertou. """
from random import randint as ran
nacertos = 0
acertos = []
for x in range(1, 6):
    a = ran(1, 100)
    b = ran(1, 100)
    n = int(input(f"{x}-Quanto é {a} + {b}? \nR: "))
    if n == (a+b):
        nacertos += 1
        acertos.append(f"{x} - Correta!")
    else: 
        acertos.append(f"{x} - Incorreta!")
for x in range(0, 5):
    print(acertos[x])
print(f"Número de acertos: {nacertos}")
