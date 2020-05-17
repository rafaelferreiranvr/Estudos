"""Faça um programa que leia três números inteiros positivos e efetue o cálculo de
uma das seguintes médias de acordo com um valor numérico digitado pelo usuário:
Geométrica, Ponderada, Harmônica ou Aritmética."""

media = int(input(
    "Médias: \n1 - Geométrica \n2- Ponderada \n3 - Harmônica \n4 - Aritmética \nTipo escolhido: "))
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))
operacoes = {
    1: (a*b*c)**(1/3),
    2: (a + 2*b + 3*c)/6,
    3: 1/(1/a + 1/b + 1/c),
    4: (a + b + c)/3
}
if a > 0 and b > 0 and c > 0:
    print(f"Resultado: {operacoes[media]}")
else:
    print("Somente valores positivos são permitidos.")
