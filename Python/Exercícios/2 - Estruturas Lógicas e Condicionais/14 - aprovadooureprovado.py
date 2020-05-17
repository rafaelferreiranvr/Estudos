"""A nota final de um estudante é calculada a partir de três notas atribuídas entre o intervalo 
de 0 até 10, respectivamente, a um trabalho de laboratório, a uma avaliação semestral 
e a um exame final. 
A média das três notas mencionadas anteriormente obedece aos 
pesos:
Trabalho de Laboratório: 2 
Avaliação Semestral: 3:
Exame Final: 5 
De acordo com o resultado, mostre na tela se o aluno está reprovado (média entre 0 e 2.9), de 
recuperação (entre 3 e 4,9) ou se foi aprovado. Faça todas as verificações necessárias. 
"""
lab = float(input("Nota do trabalho de laboratório: "))
aval = float(input("Nota da avaliação semestral: "))
exam = float(input("Nota do exame final: "))
media = (2*lab + 3*aval + 5*exam)/10 

if (0 <= lab <= 10) and (0 <= aval <= 10) and (0 <= exam <= 10):
    print(f"Média: {media}")
    if 0 <= media < 3:
        print("Reprovado.")
    elif 3 <= media < 5:
        print("Recuperação")
    elif media >= 5: 
        print("Aprovado.") 
else: 
    print("Notas inválidas.")

    
    