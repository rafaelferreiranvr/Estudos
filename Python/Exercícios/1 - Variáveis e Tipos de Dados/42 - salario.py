"""Receba o salário-base de um funcionário. Calcule e imprima o salário a receber, 
sabendo-se que esse funcionário tem uma gratificação de 5% sobre o salário-base.
Além disso, ele paga 7% de imposto sobre o salário-base. 
""" 
base = float(input("Salário-base: "))
final = base*(1 + 0.05 - 0.07)
print(f"Salário final: {final}")