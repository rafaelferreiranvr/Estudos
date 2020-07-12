#Faça um programa para ler a nota da prova de 15 alunos e armazene num vetor, calcule e imprima a média geral. 
a = []
a.append(int(input("Digite um número: ")))
soma = 0

for x in range(15):
    a.append(int(input("Digite um outro número: ")))

for x in a:
    soma += x

print(f"Média: {soma/len(a)}")
