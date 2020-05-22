# Faça um programa que some todos os números naturais abaixo de 1000 que são múltiplos de 3 ou 5.
soma = 0
for x in range(1, 1000):
    if x % 3 == 0 or x % 5 == 0:
        soma += x
print(f"Soma: {soma}")
