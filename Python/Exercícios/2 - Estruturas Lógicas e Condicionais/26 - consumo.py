"""Leia a distância em Km e a quantidade de litros de gasolina consumidos por um carro em um percurso. 
Calcule o consumo em Km/l e escreva uma mensagem de acordo com a tabela abaixo: 
CONSUMO (Km/l)        MENSAGEM 
menor que 8           Venda o carro! 
entre 8 e 12          Econômico! 
maior que 12          Super econômico! """

km = float(input("Digite a distancia em Km: "))
l = float(input("Digite a quantidade de gasolina consumida em litros: "))
consumo = km/l 

if consumo < 8: 
    print("Venda o carro!")
elif 8 <= consumo < 12:
    print("Econômico!")
else: 
    print("Super econômico!")
