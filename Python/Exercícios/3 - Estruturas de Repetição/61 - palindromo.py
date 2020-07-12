"""Faça um programa que calcule o maior número palíndromo feito a partir do produto de dois números de 3 dígitos. 
Ex: O maior palíndromo feito a partir do produto de dois números de dois dígitos é 9009 = 91*99. """
palindromos = []
solucoes = {}
i = -1
for x in range(100, 1000):
    for y in range(100, 1000):
        a = str(x*y)
        b = a[::-1]
        if a == b:
            i += 1
            palindromos.append(a)
            k = {a : f"{x} * {y} = {a}"}
            solucoes.update(k)
            k.clear()

print(f"Maior palíndromo feito a partir do produto de 2 digitos: {max(palindromos)} \nSolução: {solucoes[max(palindromos)]}")
            
