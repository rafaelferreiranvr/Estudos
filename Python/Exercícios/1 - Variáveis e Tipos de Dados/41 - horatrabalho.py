"""Faça um programa que leia o valor da hora de trabalho (em reais) e número de horas trabalhadas no mês. 
Imprima o valor a ser pago ao funcionário, adicionando 10% sobre o valor calculado. """
valor = float(input("Valor da hora de trabalho: "))
horas = float(input("Quantidade de horas trabalhadas: "))
pagamento = valor * horas * (1 + 0.1)
print(f"Pagamento: {pagamento}")
