# Faça um programa para calcular a seguinte sequência:
# S = 1 + 3 + 5 + 7 + ... + (2n - 1)
n = int(input("Digite um número: "))
s = 0
for x in range(1, n+1):
    s += (2*x - 1)
print(f"Valor de S: {s}")