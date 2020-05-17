"""Faça um programa que mostre ao usuário um menu com 4 opções de operações ma-
temáticas (as básicas, por exemplo). O usuário escolhe uma das opções e o seu pro-
grama então pede dois valores numéricos e realiza a operação, mostrando o resultado e saindo. """
operacao = int(input(
    "Operações possíveis: \n1 - Multiplicação \n2 - Adição \n3 - Subtração \n4 - Divisão \nOpção escolhida: "))

if operacao == 1 or operacao == 2 or operacao == 3 or operacao == 4 :
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))
    if operacao == 1:
        print(f"Resultado: {a * b} ")
    elif operacao == 2:
        print(f"Resultado: {a + b}")
    elif operacao == 3: 
        print(f"Resultado: {a - b}")
    elif operacao == 4: 
        print(f"Resultado: {a / b}")
else:
    print("Operação inválida")
