#Faça um programa que leia um vetor de 10 posições e verifique se existem valores iguais e os escreva na tela. 
a = []
b = {}
q = 0
for x in range(10):
    a.append(int(input("Digite um número: ")))

for x in a:
    for y in a:
        if x == y:
            q += 1
    b.update({x : q})
    q = 0

for x in b:
    if b[x] > 1:
        print(f"{x} se repetiu {b[x]} vezes")