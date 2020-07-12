"""Escreva um programa que leia o número de habitantes de uma determinada cidade, 
o valor do kwh, e para cada habitante entre com os seguintes dados: 
consumo do mês e o código do consumidor (1-Residencial. 2-Comercial, 3-Industrial). 
No final imprima o maior, o menor e a média do consumo dos habitantes: 
e por fim o total do consumo de cada categoria de consumidor. 
"""
n = int(input("Digite o número de habitantes: "))
k = []
k1 = []
k2 = []
k3 = []
n1 = 0
n2 = 0
n3 = 0
for x in range(1, n+1):
    print(f"Habitante {x}:")
    m = int(input("Categoria de Consumidor: \n1 - Residencial \n2 - Comercial \n3 - Industrial \nEscolha:  "))
    o = int(input("Consumo do habitante em kwh: "))
    k.append(o)
    if m == 1:
        k1.append(o)
    elif m == 2:
        k2.append(o)
    elif m == 3:
        k3.append(o)

print(f"Média de consumo total: {sum(k)/len(k)} \nMédia de consumo por classe: \n Residencial: {sum(k1)/len(k1)} \n Comercial: {sum(k2)/len(k2)} \n Industrial: {sum(k3)/len(k3)}")