"""Faça um programa que leia vários números, calcule e mostre: 
(a) A soma dos números digitados 
(b) A quantidade de números digitados 
(c) A média dos números digitados 
(d) O maior número digitado 
(e) O menor número digitado 
(f) A média dos números pares 
Finalize a entrada de dados caso o usuário informe o valor 0. """
n = int(input("Digite um número: "))
par = []
k = []
while n != 0:
    if n % 2 == 0:
        par.append(n)
    k.append(n)
    n = int(input("Digite um outro número: "))

print(f"Soma dos números digitados: {sum(k)} \nQuantidade de números digitados: {len(k)} \nMédia dos números digitados: {sum(k)/len(k)} \nMaior número digitado: {max(k)} \nMenor número digitado: {min(k)} \nMédia dos números pares: {sum(par)/len(par)}")

        