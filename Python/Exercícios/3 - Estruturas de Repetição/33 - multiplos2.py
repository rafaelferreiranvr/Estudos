"""Dados n e dois números inteiros positivos i e j, diferentes de 0, 
imprimir em ordem crescente os n primeiros naturais que são múltiplos de i ou de j e ou de ambos. 
Exemplo: Para n = 6, i = 2 e j = 3 a saída deverá ser: 0, 2, 3, 4, 6, 8. 
"""
n = int(input("Quantos números devem ser exibidos? "))
i = int(input("Digite um número para ser um divisor: "))
j = int(input("Digite outro número para ser um divisor: "))
numeros = []
k = 0
x = 1
while k != n:
    possibilidades = [
        x % i == 0,
        x % j == 0
    ]
    if any(possibilidades):
        numeros.append(x)
        k += 1
    x += 1
        
print(f"Multiplos de {i}, de {j} ou de ambos: ")
print(numeros)
