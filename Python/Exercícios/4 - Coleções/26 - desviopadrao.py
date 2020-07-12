#Faça um programa que calcule o desvio padrão de um vetor contendo 10 números. 
a = []
n = int(input("Digite o número de elementos do vetor: "))
for x in range(n):
    a.append(int(input("Digite um número para o vetor: ")))


m = sum(a)/len(a)
somatorio = 0
for x in a:
    somatorio += (x - m)**2
desvio = (somatorio/(n - 1))**(1/2)


print(f"Desvio padrão do vetor: {desvio}")
    
