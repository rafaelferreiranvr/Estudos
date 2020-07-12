#Crie um programa que lê 6 valores inteiros pares e, em seguida, mostre na tela os valores lidos na ordem inversa. 
a = []
a.append(int(input("Digite um número: ")))
for x in range(6):
    a.append(int(input("Digite um outro número: ")))
for x in a:
    if x % 2 != 0:
        raise TypeError("Somente números pares são permitidos.")
reversed(a)
print(a)