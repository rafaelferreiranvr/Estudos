#Leia um número inteiro e imprima a soma do sucessor de seu triplo com o antecessor de seu dobro. 
num = int(input("Digite um número: "))
soma = num * 5 #Multiplicar por 5 é a simplificação do seguinte processo: (num*3 + 1) + (num*2 - 1)
print(f"Soma: {soma}")
