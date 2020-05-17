"""Escreva um programa que, dada a idade de um nadador. classifique-o em uma das seguintes categorias:
Categoria Idade
Infantil A  5 a 7
Infantil B  8 a 10
Juvenil A 11 a 13
Juvenil B 14 a 17
Sênior  maiores de 18 anos """
idade = int(input("Digite a idade do nadador: "))
if idade > 5: 
    if 5 <= idade <= 7:
        print("Classificação: Infantil A")
    elif 8 <= idade <= 10: 
        print("Classificação: Infantil B")
    elif 11 <= idade <= 13: 
        print("Classificação: Juvenil A")
    elif 14 <= idade <= 17:
        print("Classificação: Juvenil B")
    else:
        print("Classificação: Sênior")
else:
    print("Muito jovem para se classificar.")