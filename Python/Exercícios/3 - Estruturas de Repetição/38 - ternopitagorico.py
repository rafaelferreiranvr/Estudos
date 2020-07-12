"""Faça um programa que calcule o terno pitagórico a, b, c, para o qual a + b + c = 1000. 
Um terno pitagórico é um conjunto de três números naturais, a, b, c, para a qual, 
Por exemplo: 
a² + b² = c²
"""
a = 0
b = 0
c = 0
d = 0
for x in range(1000):
    for y in range(1000):
        for z in range(1000):
            if (x + y + z == 1000) and (x**2 + y**2 == z**2):
                a = x
                b = y
                c = z
                print(f"Valores: A = {a}, B = {b}, C = {c}")

   

                
