#Leia um valor em real e a cotação do dolar, depois imprima o valor correspondente em dolares.
real = float(input("Valor em real: "))
cotacao = float(input("Cotação atual do dolar: "))
dolar = real / cotacao 
print (f"Valor em dolares: {dolar}")