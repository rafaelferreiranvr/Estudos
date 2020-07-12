"""Faça um programa que leia um vetor de 5 posições para números reais e, depois, um código inteiro. 
Se o código for zero, finalize o programa; se for 1, mostre o vetor na ordem direta,
se for 2, mostre o vetor na ordem inversa. 
Caso, o código for diferente de 1 e 2 escreva uma mensagem informando que o código é inválido. """
a = []
for x in range(5):
    a.append(int(input("Digite um número: ")))
n = int(input("0 - Finalize o programa \n1 - Exiba o vetor na ordem direta \n2 - Exiba o vetor em ordem invertida \nEscolha: "))
if n == 1:
    print(a)
elif n == 2:
    a.reverse()
    print(a)