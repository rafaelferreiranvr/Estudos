# Faca um algoritmo que leia um número positivo e imprima seus divisores.
n = int(input("Digite um número: "))
print("Divisores desse número: ")
for x in range(1, n+1):
    if n % x == 0:
        if x == n:
            print(x)
        else:
            print(x, end=", ")
