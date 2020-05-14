"""Faça um programa que leia um número e, caso ele seja positivo, calcule e mostre:
O número digitado ao quadrado 
A raiz quadrada do número digitado 
"""
num = float(input("Número: "))
if num > 0:
    print(f"Raíz do número: {num**(1/2)} \nNúmero ao quadrado: {num**2}")
else: 
    print("Número inválido")