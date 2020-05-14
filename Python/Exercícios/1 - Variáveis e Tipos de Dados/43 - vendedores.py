"""Escreva um programa de ajuda para vendedores. A partir de um valor total lido, mostre:
o total a pagar com desconto de 10%; 
o valor de cada parcela, no parcelamento de 3x sem juros; 
a comissão do vendedor, no caso da venda ser a vista (5% sobre o valor com desconto) 
a comissão do vendedor, no caso da venda ser parcelada (5% sobre o valor total) """
valor = float(input("Valor total: "))
valorcomdesconto = valor * (1 - 0.1)
parcela = valor/3
comissaoavista = valorcomdesconto*0.05
comissaoparcelada = valor*0.05
print(f"Total com desconto: {valorcomdesconto} \nValor da parcela: {parcela} \nCommissão do vendedor(a vista): {comissaoavista} \nComissão do vendedor(parcelado): {comissaoparcelada}")