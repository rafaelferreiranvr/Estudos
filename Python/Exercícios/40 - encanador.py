''' Uma empresa contrata um encanador a R$ 30,00 por dia. 
Faça um programa que solicite o número de dias trabalhados pelo encanador e imprima
a quantia líquida que deverá ser paga, sabendo-se que são descontados 8% para imposto de renda. '''
dias = int(input("Dias trabalhados: "))
valor = 30*dias
valor = valor * (1 - 0.08)
print(f"Deve ser pago {valor} reais ao encanador.")