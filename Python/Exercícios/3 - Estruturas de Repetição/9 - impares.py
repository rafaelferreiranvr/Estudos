# Faça um programa que leia um número inteiro N e depois imprima os N primeiros números naturais ímpares.
n = int(input("Digite um número: "))
print(f"{n} primeiros números ímpares: ")
for x in range(1, n+1):
    m = 2*x - 1
    if x == (n-1):
        print(m, end=" e ")
    elif x == (n):
        print(m)
    else:
        print(m, end=", ")
