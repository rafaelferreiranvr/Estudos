"""As tarifas de certo parque de estacionamento são as seguintes: 
• 1 e 2 hora - R$ 1,00 cada 
• 3 e 4 hora - R$ 1,40 cada 
• 5 hora e seguintes - R$ 2,00 cada 
O número de horas a pagar é sempre inteiro e arredondado por excesso. 
Deste modo, quem estacionar durante 61 minutos pagará por duas horas, 
que é o mesmo que pagaria se tivesse permanecido 120 minutos. 
Os momentos de chegada ao parque e partida deste são apresentados na forma de pares de inteiros, 
representando horas e minutos. 
Por exemplo, o par 12 50 representará "dez para a uma da tarde''. 
Pretende-se criar um programa que, lidos pelo teclado os momentos de chegada e de partida, escreva na tela o preço cobrado pelo estacionamento. 
Admite-se que a chegada e a partida se dão com intervalo não superior a 24 horas. 
Portanto, se uma dada hora de chegada for superior à da partida, isso não é uma situação de erro, 
antes significará que a partida ocorreu no dia seguinte ao da chegada. """
chegada = input("Digite a hora de chegada: ").split(" ")
partida = input("Digite a hora de partida: ").split(" ")

for x in range(1):
    chegada[x] = int(chegada[x])
    partida[x] = int(partida[x])

if chegada[1] == partida[1]:
    if chegada[0] > partida[0]:
        diferenca = 24 - (chegada[0] - partida[0])
    else:
        diferenca = partida[0] - chegada[0]
else:
    if chegada[0] > partida[0]:
        diferenca = 24 - (chegada[0] - partida[0]) + 1
    else:
        diferenca = partida[0] - chegada[0] + 1


tarifas = {
    diferenca == 1 or diferenca == 2 : diferenca,
    diferenca == 3 or diferenca == 4 : diferenca + (diferenca*1.4),
    diferenca >= 5 : diferenca + (diferenca*1.4) + (diferenca*2)
}

print(f"Tarifa: {tarifas[True]:.2f}")