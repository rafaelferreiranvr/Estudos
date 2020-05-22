# Faça um programa para calcular a seguinte sequência:
# S = 1 + 2 + 3 + 4 + 5 + ... + n
n = int(input("Digite um número: "))
s = 0
for x in range(n+1):
    s += x
print(f"Valor de S: {s}")