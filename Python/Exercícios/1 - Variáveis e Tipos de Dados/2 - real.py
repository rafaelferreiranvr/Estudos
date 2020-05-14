# Faça um programa que leia um número real e o imprima
numero = complex(input("Digite um número: "))
real = float(numero.real)
imag = float(numero.imag)
if imag==0:
    print(real)
else:
    print("ERRO! Somente números reais são permitidos")
