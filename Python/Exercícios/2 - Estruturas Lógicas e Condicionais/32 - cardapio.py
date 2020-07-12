"""Escrever um programa que leia o código do produto escolhido do cardápio de uma lanchonete e a quantidade. 
O programa deve calcular o valor a ser pago por aquele lanche.
Considere que a cada execução somente será calculado um pedido. 
O cardápio da lanchonete segue o padrão abaixo: 
Especificação      Código       Preço 
Cachorro Quente     100          1.20
Bauru Simples       101          1.30 
Bauru com Ovo       102          1.50
Hamburguer          103          1.20 
Cheeseburguer       104          1.70 
Suco                105          2.20 
Refrigerante        106          1.00 
"""
codigo = int(input("Digite o código do produto: "))
quantidade = int(input("Digite a quantidade: "))

cardapio = {
    100 : 1.20,
    101 : 1.30,
    102 : 1.50,
    103 : 1.20,
    104 : 1.70,
    105 : 2.20, 
    106 : 1.00
}

print(f"Valor a ser pago: {cardapio[codigo]*quantidade}")