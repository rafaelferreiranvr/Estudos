#Faça um programa que receba dois números e mostre o maior. 
# Se por acaso, os dois números forem iguais, imprima a mensagem números iguais. 
a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))

if a != b:
    if a > b:
        print(f"{a} é maior que {b}.")
    else:
        print(f"{b} é maior que {a}.")
else:
    print("Números iguais.")