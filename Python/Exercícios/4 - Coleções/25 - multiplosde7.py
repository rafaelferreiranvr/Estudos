"""Faça um programa que preencha um vetor de tamanho 100 com os 100 primeiros 
naturais que não são múltiplos de 7 ou que terminam com 7. 
"""
a = []
n = 0
i = 0
while n != 100:
    i += 1
    if int(str(i)[len(str(i)) - 1]) != 7 and i % 7 != 0:
        a.append(i)
        n += 1
print(f"100 primeiros números que não terminam com 7 e nem são multiplos de 7: {a}")
        