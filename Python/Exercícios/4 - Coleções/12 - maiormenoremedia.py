#Fazer um programa para ler 5 valores e, em seguida, mostrar todos os valores lidos juntamente com o maior, o menor e a média dos valores. 
a = []
a.append(int(input("Digite um número: ")))
soma = 0

for x in range(5):
    a.append(int(input("Digite um outro número: ")))

for x in a:
    soma += x
print(f"Maior valor: {max(a)}, Menor valor: {min(a)}, Média dos valores: {soma/len(a)}")                            