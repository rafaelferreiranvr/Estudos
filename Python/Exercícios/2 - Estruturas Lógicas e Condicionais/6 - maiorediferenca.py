#Escreva um programa que, dados dois números inteiros, mostre na tela o maior deles.
#Assim como a diferença existente entre ambos. 
a = float(input("Digite um número: "))
b = float(input("Digite outro número: "))
if a > b:
    print(f"{a} é maior que {b}. A diferença entre eles é de {a - b}")
else:
    print(f"{b} é maior que {a}. A diferença entre eles é de {b - a}")