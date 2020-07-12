"""Um funcionário recebe aumento anual. Em 1995 foi contratado por 2000 reais. 
Em 1996 recebeu aumento de 1.5%. A partir de 1997,
os aumentos sempre correspondem ao dobro do ano anterior. 
Faça programa que determine o salário atual do funcionário."""
salario = 2000
aumento = (1.5/100)
salario = salario + 2000*aumento
ano = 1996
while ano < 2020:
    ano += 1
    aumento *= 2
    salario = salario + 2000*aumento

print(f"Salário em {ano}: {salario}")