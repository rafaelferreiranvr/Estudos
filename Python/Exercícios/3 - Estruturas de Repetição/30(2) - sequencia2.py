# Faça um programa para calcular a seguinte sequência:
# S = 1 - 2 + 3 - 4 + 5 - 6 + ...
n = int(input("Digite um número: "))
s = 0
for x in range(2, n+1):
    s += ((x-1) - x)
print(f"Valor de S: {s}")
