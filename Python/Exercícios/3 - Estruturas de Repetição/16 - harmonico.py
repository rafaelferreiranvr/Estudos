"""Em Matemática, o número harmônico designado por H(n) define-se como sendo a soma da série harmônica: 
H(n) = 1+ 1/2 + 1/3 + 1/4 +...+ 1/n 
Faça um programa que leia um valor n inteiro e positivo e apresente o valor de H(n). """
n = int(input("Digite um número: "))
soma = 1
for x in range(2, n+1):
    soma += (1/x)
print(f"H({n})={soma}")
