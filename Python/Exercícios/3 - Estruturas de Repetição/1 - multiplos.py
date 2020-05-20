"""Faça um programa que determine o mostre os N primeiros múltiplos de M, conside-
rando números maiores que 0.""" 
n = int(input("Quantos multiplos deverão ser exibidos? "))
m = int(input("Multiplos de que número devem ser exibidos? "))
b = []
for x in range(1, n+1):
    b.append(x*m)
print(f"{n} primeiros multiplos de {m}: ")
for x in range(len(b)):
    if x==(len(b) - 1):
        print(b[x])
    elif x==(len(b) - 2):
        print(b[x], end=" e ")
    else:
        print(b[x], end=", ")
