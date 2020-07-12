"""Faça um programa que leia dois conjuntos de dez valores. o primeiro representando o número do aluno e o segundo representando a sua altura em metros. 
Encontre o aluno mais baixo e o mais alto. 
Mostre o número do aluno mais baixo e do mais alto, juntamente com suas alturas. 
"""
c = []
a = []
par = {}
for x in range(10):
    c.append(int(input("Digite o código do aluno: " ))) 
    a.append(float(input("Digite a altura desse aluno: ")))
for x in range(10):
    par.update({a[x]:c[x]})
print(f"Código do aluno mais alto: {par[max(a)]}, Maior Altura: {max(a)} \nCódigo do aluno mais baixo: {par[min(a)]}, Menor altura: {min(a)}")





    
    

