"""Escreva o menu de opções abaixo. Leia a opção do usuário e execute a operação esco-
lhida. Escreva uma mensagem de erro se a opção for inválida. 
Escolha a opção: 
1- Soma de 2 números. 
2- Diferença entre 2 números (maior pelo menor). 
3- Produto entre 2 números. 
4- Divisão entre 2 números (o denominador não pode ser zero)."""
operacao = int(input(
    "Escolha a opção: \n1- Soma de 2 números. \n2- Diferença entre 2 números (maior pelo menor). \n3- Produto entre 2 números. \n4- Divisão entre 2 números (o denominador não pode ser zero)."))

if 1 >= operacao <= 3:
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))
    if operacao == 1:
        print(f"Resultado: {a + b} ")
    elif operacao == 2:
        if a > b:
            print(f"Resultado: {a - b}")
        else:
            print("Operação não reconhecida.")
    elif operacao == 3:
        print(f"Resultado: {a * b}")
elif operacao == 4:
    a = float(input("Digite o numerador: "))
    b = float(input("Digite o denominador: "))
    if b == 0:
        print("Operação impossível")
    else:
        print(f"Resultado: {a / b}")
else:
    print("Operação inválida.")
