"""O custo ao consumidor de um carro novo é a soma do custo de fábrica, da comissão do distribuidor, 
e dos impostos. A comissão e os impostos são calculados sobre o custo de fábrica, 
de acordo com a tabela abaixo. Leia o custo de fábrica e escreva o custo ao consumidor. 
CUSTO DE FÁBRICA            % DO DISTRIBUIDOR          % DOS IMPOSTOS 
até R$12.000,00                     5                      isento
entre R$12.000,00 e 25.000,00       10                       15 
acima de R$25.000.00                15                       20 
"""
custo = float(input("Digite o custo de fábrica: "))

distribuidor = {
    custo < 12000 : custo*0.05,
    12000 <= custo <= 25000 : custo*0.1,
    25000 < custo : custo*0.15
}

impostos = {
    custo < 12000 : 0,
    12000 <= custo <= 25000 : custo*0.15,
    25000 < custo : custo*0.20
}

print(f"Preço para o consumidor: {custo + distribuidor[True] + impostos[True]}")
