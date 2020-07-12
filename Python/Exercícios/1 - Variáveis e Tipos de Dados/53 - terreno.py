"""Faça um programa para ler as dimensões de um terreno (comprimento c e largura l), bem como o preço do metro de tela p. 
Imprima o custo para cercar este mesmo terreno com tela.""" 
c = float(input("Digite o comprimento desse terreno: "))
l = float(input("Digite a largura desse terreno: "))
preco = float(input("Digite o valor do metro de tela: "))
valor = 2*preco*(c+l) 
print(f"Valor a ser pago: {valor}")