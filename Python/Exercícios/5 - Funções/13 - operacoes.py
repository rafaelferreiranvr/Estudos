"""Faça uma função que receba dois valores numéricos e um símbolo.
Este símbolo representará a operação que se deseja efetuar com os números.
Se o símbolo for '+', deverá ser realizada uma adição, se for '-',
uma subtração, se for '/', uma divisão e se for '*' será efetuada uma
multiplicação.
"""
a = int(input("Digite um valor: "))
b = int(input("Digite um outro valor: "))
s = input("""Opções: \n+ = Soma \n* = Multiplicação \n/ = Divisão
- = Subtração \nOpção escolhida: """)


def operacoes(x, y, z):
    if a <= 0 or b <= 0:
        raise ValueError("Só são permitidos valores maiores do que 0.")
    else:
        op = {
            '+': x + y,
            '*': x * y,
            '-': x - y,
            '/': x / y
        }
        return op[f'{z}']


print(f"Resultado a operação: {operacoes(a, b, s)}")
