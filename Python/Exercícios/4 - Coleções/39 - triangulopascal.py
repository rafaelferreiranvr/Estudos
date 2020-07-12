"""Escreva um programa que leia um número inteiro positivo n e em seguida 
imprima n linhas do chamado Triangulo de Pascal: 
1 
1 1 
1 2 1 
1 3 3 1 
1 4 6 4 1
1 5 10 10 5 1 
....."""
def fatorial(m):
    if m == 0:
        m = 1
    elif m == 1:
        m = 1
    else:
        for x in range(m-1, 0, -1):
            m *= x
    return m
def binomial(n, p):
    b = fatorial(n)/(fatorial(p)*fatorial(n-p))
    return b
n = int(input("Até qual linha do triângulo de Pascal você deseja imprimir? "))

k = 0
l = 0
while k != (n+1):
    for x in range(k+1):
        print(int(binomial(k, l)), end=" ")
        l += 1 
        if x == k:
            print()
    k += 1
    l = 0


        
        
            
    

    

      