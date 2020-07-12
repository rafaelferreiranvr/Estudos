"""Leia uma data e determine se ela é válida. Ou seja, verifique se o mês está entre 1 e 12, e se o dia existe naquele mês.
Note que Fevereiro tem 29 dias em anos bissextos. e 28 dias em anos não bissextos. 
"""
data = input("Digite a data (Dia/mês/ano): ")
data = data.split("/")
for x in range(len(data)):
    data[x] = int(data[x])
dia = data[0]
mes = data[1]
ano = data[2]

dias31 = [1, 3, 5, 7, 8, 10, 12]
dias30 = [4, 6, 9, 11]
dias29 = [2]

confirmacao = False

if mes in dias31:
    if 1 <= dia <= 31:
        confirmacao = True
elif mes in dias30:
    if 1 <= dia <= 30:    
        confirmacao = True
elif mes in dias29:
    if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
        if 1 <= dia <= 29:
            confirmacao = True
    else:
        if 1 <= dia <= 28:
            confirmacao = True

if confirmacao:
    print("Data válida.")
else:
    print("Data inválida")