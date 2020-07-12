"""Escreve um programa que verifique quais números entre 1000 e 9999 (inclusive) pos-
suem a propriedade seguinte: 
a soma dos dois dígitos de mais baixa ordem com os dois dígitos de mais alta ordem elevada ao quadrado é igual ao próprio numero. 
Por exemplo, para o inteiro 3025, temos que: 30 + 25 = 55
55² = 3025 
"""
lista = []
for x in range(1000, 10000):
    a = str(x)
    b = int(a[0] + a[1])
    c = int(a[2] + a[3])
    if (b + c)**2 == x:
        lista.append(x)
print(f"Números com essa propriedade: {lista}")