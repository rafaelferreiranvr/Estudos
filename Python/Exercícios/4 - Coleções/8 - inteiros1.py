#Crie um programa que lê 6 valores inteiros e, em seguida, mostre na tela os valores lidos na ordem inversa. 
a = []
a.append(int(input("Digite um número: ")))
for x in range(6):
    a.append(int(input("Digite um outro número: ")))

reversed(a)
print(a)