#Escreva um programa que leia as coordenadas X e Y de pontos no plano cartesiano e calcule sua distancia de origem(0,0).
x = float(input("Digite a coordenada x: "))
y = float(input("Digite a coordenada y: "))
distancia = (x**2 + y**2)**(1/2)
print(f"Distância da origem: {distancia}")