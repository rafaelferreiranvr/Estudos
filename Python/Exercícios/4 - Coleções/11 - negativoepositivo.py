#Faça um programa que preencha um vetor com 10 números reais, calcule e mostre a quantidade de números negativos e a soma dos números positivos desse vetor. 
a = []
b = []
soma = 0
n = 0
a.append(int(input("Digite um número: ")))

for x in range(0, 10):
    a.append(int(input("Digite um outro número: ")))
    
for x in a:
    if x > 0:  
        soma += x
    else:
        n += 1
        
print(f"Soma dos números positivos: {soma} \nQuantidade de números negativos: {n}")