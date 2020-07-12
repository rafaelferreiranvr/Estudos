"""Três amigos jogaram na loteria. Caso eles ganhem, o prêmio deve ser repartido proporcionalmente ao valor que cada deu para a realização da aposta.
Faça um programa que leia quanto cada apostador investiu, o valor do prêmio, e imprima quanto cada um ganharia do prémio com base no valor investido. """
a = float(input("Contribuição do primeiro amigo: "))
b = float(input("Contribuição do segundo amigo: "))
c = float(input("Contribuição do terceiro amigo: "))
total = a + b + c 
a = a*100/total
b = b*100/total
c = c*100/total
print(f"O primeiro amigo recebe {a}% do prêmio \nO segundo amigo recebe {b}% \nO terceiro amigo recebe {c}%")