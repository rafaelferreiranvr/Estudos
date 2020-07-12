"""Faça um programa que apresente um menu de opções para o cálculo das seguintes operações entre dois números: 
• adição (opção 1) 
• subtração (opção 2) 
• multiplicação (opção 3) 
• divisão (opção 4).
• saída (opção 5) 
O programa deve possibilitar ao usuário a escolha da operação desejada,
a exibição do resultado e a volta ao menu de opções. 
O programa só termina quando for escolhida a opção de saída (opção 5). 
"""
n = 0
a = 0
b = 0
while n != 5:
    n = int(input("1 - Adição \n2 - Subtração \n3 - Multiplicação \n4 - Divisão \n5 - Saída \nEscolha: "))
    a = int(input("Digite o primeiro número: "))
    b = int(input("Digite o segundo número: "))

    operacoes = {
        1 : a + b,
        2 : a - b,
        3 : a * b,
        4 : a / b,
    }
    
    print(f"Resultado: {operacoes[n]}")
