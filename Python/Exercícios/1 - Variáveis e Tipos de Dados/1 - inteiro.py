# Faça um programa que leia um número inteiro e o imprima
numero = complex(input("Digite um número: "))
real = float(numero.real)
imag = float(numero.imag)
if real % 1 ==0 and imag==0:
    print(real)
else:
    print("ERRO! Somente números inteiros são permitidos")
