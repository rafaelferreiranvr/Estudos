# Faça uma função que calcule o maior fator primo de um número.
n = int(input("Digite um número: "))


def maiorfator(x):
    fatores = []
    FatoresPrimos = []
    for y in range(1, x+1):
        if x % y == 0:
            fatores.append(y)

    for y in fatores:
        DivisoresDoFator = []
        for z in range(1, y+1):
            if y % z == 0:
                DivisoresDoFator.append(z)
        if len(DivisoresDoFator) == 2:
            FatoresPrimos.append(y)
    return max(FatoresPrimos)


print(f"Maior fator primo de {n}: {maiorfator(n)}")
