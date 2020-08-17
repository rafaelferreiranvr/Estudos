"""Escreva uma função que receba um número inteiro maior do que zero e
retorne a soma de todos os seus algarismos.
Por exemplo, ao número 251 corresponderá o valor 8 (2 + 5 + 1).
Se o número lido não for maior do que zero, o programa terminará com a
mensagem "Número inválido".
"""
n = input("Digite um número: ")
if int(n) <= 0:
    raise ValueError("Digite um valor maior que 0.")


def soma(x):
    soma = 0
    for x in n:
        soma += int(x)
    return soma


print(f"Soma dos algarísmos do número digitado: {soma(n)}")
