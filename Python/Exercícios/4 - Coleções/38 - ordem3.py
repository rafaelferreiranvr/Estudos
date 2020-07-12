"""Peça ao usuário para digitar dez valores numéricos e ordene por ordem crescente esses valores, 
guardando-os num vetor. 
Ordene o valor assim que ele for digitado, 
mostre ao final na tela os valores em ordem. 
"""
a = []
for x in range(10):
    a.append(int(input("Digite um número: ")))
    a.sort()
    print(a)
print(f"Vetor ordenado: {a}")