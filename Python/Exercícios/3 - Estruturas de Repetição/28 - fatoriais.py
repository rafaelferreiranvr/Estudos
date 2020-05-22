"""Faça um programa que leia um valor V inteiro e positivo. calcule o mostre o valor E. 
Conforme a fórmula a seguir: 
E = 1+1/1! + 1/2! + 1/3! +... + 1/N! """


def fatorial(a):
    f = a
    for x in range(1, a):
        f *= (a-x)
    return f


n = int(input("Digite um valor: "))
e = 1
for x in range(1, n+1):
    e += (1/(fatorial(x)))
print(f"Valor de E: {e}")
