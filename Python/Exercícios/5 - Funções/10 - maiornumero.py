# Faça uma função que receba dois números e retorne qual deles é o maior.

a = float(input("Digite um número: "))
b = float(input("Digite outro número: "))


def maior(x, y):
    if x > y:
        return x
    else:
        return y


print(f"O maior número é: {maior(a, b)}")
