'''Leia o salário de um trabalhador e o valor da prestação de um empréstimo.
Se a prestação for maior que 20% do salário imprima: Empréstimo não concedido,
caso contrário, imprima: Empréstimo concedido. '''
salario = float(input("Salário: "))
emprestimo = float(input("Empréstimo: "))

if emprestimo <= (salario*0.2): 
    print("Empréstimo condedido.")
else:
    print("Empréstimo negado.")
    