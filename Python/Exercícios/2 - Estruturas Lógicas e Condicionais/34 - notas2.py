"""Leia a nota e o número de faltas de um aluno. e escreva seu conceito.
De acordo com a tabela abaixo, quando o aluno tem mais de 20 faltas ocorre uma redução de conceito. 
NOTA                     CONCEITO (ATE 20 FALTAS)         CONCEITO (MAIS DE 20 FALTAS) 
de 9(incluso) a 10(incluso)         A                                 B
de 7.5(incluso) a 9                 B                                 C
de 5(incluso) a 7.5                 C                                 D
de 4(incluso) a 5                   D                                 E
de 0(incluso) a 4                   E                                 E
"""

nota = float(input("Nota do aluno: "))
faltas = float(input("Número de faltas do aluno: "))
conceito = " "
if faltas <= 20:
    if 9 <= nota <= 10:
        conceito = "A"
    elif 7.5 <= nota < 9:
        conceito = "B"
    elif 5 <= nota < 7.5:
        conceito = "C"
    elif 4 <= nota < 5:
        conceito = "D"
    else:
        conceito = "E"
else:
    if 9 <= nota <= 10:
        conceito =  "B"
    elif 7.5 <= nota < 9:
        conceito = "C"
    elif 5 <= nota < 7.5:
        conceito = "D"
    elif 4 <= nota < 5:
        conceito = "E"
    else:
        conceito = "E"
        
print(f"Conceito: {conceito} ")