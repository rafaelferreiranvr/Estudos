"""Faça um programa que calcule a diferença entre a soma dos quadrados dos 
primeiros 100 números naturais e o quadrado da soma. """
soma = 0
somaquadrado = 0 


for x in range(1, 101):
    soma += x**2
    somaquadrado += x


somaquadrado = somaquadrado**2
print(f"Soma de quadrados: {soma} \nQuadrado da soma: {somaquadrado} \nDiferença: {somaquadrado - soma}")