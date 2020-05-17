# Faça um programa para verificar se um determinado número inteiro e divisível por 3 ou 5, mas não simultaneamente pelos dois.
num = int(input("Digite um número: "))
if (num % 3 == 0):
    print("Esse número é divisível por 3.")
elif (num % 5 == 0):
    print("Esse número é divisível por 5.")
elif (num % 3 == 0) and (num % 5 == 0):
    print("Esse número é divisível por 3 e por 5.")
else:
    print("Esse número não é divisível nem por 3 e nem por 5.")    
