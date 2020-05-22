# Faça um programa para calcular a seguinte sequência:
# S = 1/1 + 3/2 + 5/3 + 7/4 +...+ 99/50
n = int(input("Digite um número: "))
s = 0
for x in range(1, n+1):
    s += (2*x - 1)/x
print(f"Valor de S: {s}")