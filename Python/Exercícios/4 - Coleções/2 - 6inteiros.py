#Crie um programa que lê 6 valores inteiros e, em seguida, mostre na tela os valored lidos. 
a = []
a.append(int(input("Digite um número: ")))
for x in range(0, 6):
    a.append(int(input("Digite um outro número: ")))
for x in a:
    print(x)
    