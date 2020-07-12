"""Faça um programa que receba a altura e o peso de uma pessoa. De acordo com a tabela a seguir, verifique e mostra qual a classificação dessa pessoa. 
Altura                                                Peso 
                  Até 60               Entre 60 e 90 (Inclusive)                   Acima de 90 
Menor que 1.20       A                            D                                      G    
De 1,20 a 1,70       B                            E                                      H
Maior que 1,70       C                            F                                      I 
"""
peso = int(input("Digite o peso: "))
altura = float(input("Digite a altura: "))
classificacao = " "

if peso < 60:
    if altura < 1.20:
        classificacao = "A"
    elif 1.20 <= altura <= 1.70:
        classificacao = "B"
    else:
        classificacao = "C"
        
elif 60 <= peso <= 90:
    if altura < 1.20:
        classificacao = "D"
    elif 1.20 <= altura <= 1.70:
        classificacao = "E"
    else:
        classificacao = "F"
else:
    if altura < 1.20:
        classificacao = "G"        
    elif 1.20 <= altura <= 1.70:
        classificacao = "H"
    else:
        classificacao = "I"

print(f"Classificação: {classificacao}")