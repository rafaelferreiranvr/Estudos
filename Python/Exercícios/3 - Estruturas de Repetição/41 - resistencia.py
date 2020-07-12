"""Faça um programa que calcula a associação em paralelo de dois resistores R1 e R2
fornecidos pelo usuário via teclado.
O programa fica pedindo estes valores e calculando até que 
o usuário entre com um valor para resistência igual a zero. 
"""
ra = 0
rb = 0
while ra >= 0 and rb >= 0:
    ra = float(input("Digite a resistência 1: "))
    rb = float(input("Digite a resistência 2: "))
    resultante = (ra*rb)/(ra + rb)
    if ra > 0 and rb > 0:
        print(f"Resistência resultante: {resultante}")
    else:
        print("Programa finalizado")
    
    