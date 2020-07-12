"""Faça um algoritmo que converta uma velocidade expressa em km/h para m/s, e vice versa. 
Você deve criar um menu com as duas opções de conversão e com uma opção para finalizar o programa. 
O usuário poderá fazer quantas conversões desejar, sendo que o programa só será finalizado quando a opção de finalizar for escolhida. """
n = int(input("1 - Km/h para M/s \n2 - M/s para Km/h \n3 - Finalizar \nOpção escolhida: "))
k = 0
m = 0
while n != 3:
    if n == 1:
        k = float(input("Digite a velocidade em km/s: "))
        m = k / 3.6 
        print(f"Velocidade em m/s: {m}")
    elif n == 2:
        m = float(input("Digite a velocidade em m/s: "))
        k = m * 3.6
        print(f"Velocidade em km/h: {k}")
    n = int(input("1 - Km/h para M/s \n2 - M/s para Km/h \n3 - Finalizar \nOpção escolhida: "))
