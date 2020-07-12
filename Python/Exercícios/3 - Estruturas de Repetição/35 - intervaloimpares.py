"""Faça um programa que some os números impares contidos em um intervalo 
definido pelo usuário. 
O usuário define o valor inicial do intervalo e o valor final deste intervalo 
e o programa deve somar todos os números ímpares contidos neste intervalo.
Caso o usuário digite um intervalo inválido 
(começando por um valor maior que o valor final) deve ser escrito uma mensagem
de erro na tela, "Intervalo de valores inválido" e o programa termina."""
a = int(input("Digite o início do intervalo: "))
b = int(input("Digite o final do intervalo: "))
soma = 0
if a > b:
    raise TypeError("Intervalo inválido.")

for x in range(a, b+1):
    if x % 2 != 0:
        soma += x

print(f"Soma: {soma}")