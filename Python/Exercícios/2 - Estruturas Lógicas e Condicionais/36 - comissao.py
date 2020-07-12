"""Escreva um programa que, dado o valor da venda, imprima a comissão que deverá ser paga ao vendedor. Para calcular a comissão, considere a tabela abaixo: 
Venda mensal                                                             Comissão 
Maior ou igual a R$100.000,00                                     R$700,00 + 16% das vendas 
Menor que R$100.000,00 e maior ou igual a R$80.000.00             R$650.00 +14% das vendas 
Menor que R$80.000,00 e maior ou igual a R$60.000.00              R$600.00 +14% das vendas 
Menor que R$60.000,00 e maior ou igual a R$40.000,00              R$550.00 +14% das vendas 
Menor que R$40.000,00 e maior ou igual a R$20.000,00              R$500.00 +14% das vendas 
Menor que R$20.000,00                                             R$400.00 +14% das vendas """

vendas = int(input("Digite o valor das vendas: "))

condicoes = {
    vendas >= 100000 : (vendas*0.16 + 700),
    100000 > vendas >= 80000 : (vendas*0.14 + 650),
    80000 > vendas >= 60000 : (vendas*0.14 + 600),
    60000 > vendas >= 40000 : (vendas*0.14 + 550),
    40000 > vendas >= 20000 : (vendas*0.14 + 500),
    vendas < 20000 : (vendas*0.14 + 400)
}

print(f"Comissão: {condicoes[True]}")

