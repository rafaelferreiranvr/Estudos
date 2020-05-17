"""Faça um algoritmo que calcule a média ponderada das notas de 3 provas. 
A primeira e a segunda prova têm peso 1 e a terceira tem peso 2. 
Ao final, mostrar a média do aluno e indicar se o aluno foi aprovado ou reprovado. 
A nota para aprovação deve ser igual ou superior a 60 pontos. 
"""
nota1 = float(input("Nota da prova 1: "))
nota2 = float(input("Nota da prova 2: "))
nota3 = float(input("Nota da prova 3: "))
media = (nota1 + nota2 + 2*nota3)/4
if media > 60:
    print(f"Aprovado com média {media}")
else: 
    print(f"Reprovado com média {media}")