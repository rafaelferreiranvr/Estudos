#Fazer um programa para ler 5 valores e, em seguida. mostrar a posição onde se encontram o maior e o menor valor. 
a = []
a.append(int(input("Digite um número: ")))
for x in range(5):
    a.append(int(input("Digite um outro número: ")))
print(f"Posição do maior valor: {a.index(max(a))}, Posição do menor valor: {a.index(min(a))}")