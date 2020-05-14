"""Leia um número fornecido pelo usuário.
Se esse número for positivo, calcule a raiz quadrada do número. 
Se o número for negativo, mostre uma mensagem dizendo que o número é inválido. """
num = float(input("Digite um número: "))
if num > 0: 
    print(f"Raíz desse número: {num**(1/2)}")
else:
    print("Número inválido")