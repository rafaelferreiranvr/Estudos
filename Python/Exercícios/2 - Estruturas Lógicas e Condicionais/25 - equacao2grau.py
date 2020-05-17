# Calcule as raízes de uma equação do segundo grau.
print("Digite os 3 coeficientes da equação de segundo grau segundo o formato ax² + bx + c.")
a = float(input("Coeficiente a: "))
b = float(input("Coeficiente b: "))
c = float(input("Coeficiente c: "))

if a != 0:
    delta = b**2 - 4*a*c
    if delta > 0:
        p = ((delta)**(1/2))/2*a
        q = -b/2*a
        print(f"Raíz 1: {q + p}")
        print(f"Raíz 2: {q - p}")
    elif delta == 0:
        print(f"Raíz única: {q}")
    else:
        print("Essa equação não possui raízes reais.")
else:
    print("Não é uma equação do segundo grau.")
