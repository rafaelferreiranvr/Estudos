"""Faça um programa que leia dois números (a e b) (positivos menores que 10000) e: 
• Crie um vetor onde cada posição é um algarismo do número. A primeira posição é o algarismo menos significativo: 
• Crie um vetor que seja a soma de a e b, mas faça-o usando apenas os vetores construídos anteriormente. 
Dica: some as posições correspondentes. 
Se a soma ultrapassar 10, subtraia 10 do resultado e some 1 à próxima posição. 
"""
a = str(int(input("Digite um número: ")))
b = str(int(input("Digite um outro número: ")))


if a > b:
    max = a
    if len(a) - len(b) != 0:
        b = b[::-1]
        for x in range(len(a) - len(b)):
            b += "0"
        b = b[::-1]

else:
    max = b
    if len(b) - len(a) != 0:
        a = a[::-1]
        for x in range(len(b) - len(a)):
            a += "0"
        a = a[::-1]


a = a[::-1]
a += "0"
a = a[::-1]
b = b[::-1]
b += "0"
b = b[::-1]

        
av = []
bv = []
cv = []
for x in a:
    av.append(int(x))
for x in b:
    bv.append(int(x))
for x in range(len(max) + 1):
    cv.append(0)

i = -1
while True:
    try:
        cv[i] += (av[i] + bv[i])
        if cv[i] >= 10:
            cv[i-1] = int(str(cv[i])[0])
            cv[i] -= int(f"{cv[i-1]}0")
        i -= 1
    except IndexError:
        break
r = ""
for x in cv:
    r += f"{x}"
print(f"Resultado: {int(r)}")
    

    