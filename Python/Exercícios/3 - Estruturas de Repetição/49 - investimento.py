"""O funcionário chamado Carlos tem um colega chamado João que recebe um salário que equivale a um terço do seu salário. 
Carlos gosta de fazer aplicações na caderneta de poupança e vai aplicar seu salário integralmente nela, pois está rendendo 2% ao mês. 
João aplicará seu salário integralmente no fundo de renda fixa, que está rendendo 5% ao mês. 
Construa um programa que deverá calcular e mostrar a quantidade de meses necessários para que o valor pertencente a João iguale ou ultrapasse o valor pertencente a Carlos. 
"""
carlos = 300
joao = 100
meses = 0
while carlos > joao:
    meses += 1
    carlos *= 1.02
    joao *= 1.05
print(f"Meses necessários para que João ultrapasse Carlos: {meses} \nValor de João: {joao} \nValor de Carlos: {carlos}")