"""Chico tem 1.50 metro e cresce 2 centímetros por ano, enquanto Zé tem 1.10 metros e cresce 3 centímetros por ano.
Escreva um programa que calcule e imprima quantos anos serão necessários para que Zé seja maior que Chico. """
chico = 1.5 
ze = 1.1
meses = 0
while chico > ze:
    meses += 1
    chico += 0.02 
    ze += 0.03
print(f"Meses necessários para que Ze fique mais alto que Chico: {meses} \nAltura de Chico: {chico} \n Altura de Zé: {ze}")