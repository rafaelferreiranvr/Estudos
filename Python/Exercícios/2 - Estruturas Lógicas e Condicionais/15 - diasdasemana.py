# Escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia da semana correspondente a este numero.
# Isto é, domingo se 1, segunda-feira se 2. e assim por diante.
numero = input("Digite um número: ")
A = {
    "1": "Domingo",
    "2": "Segunda-feira",
    "3": "Terça-feira",
    "4": "Quarta-feira",
    "5": "Quinta-feira",
    "6": "Sexta-feira",
    "7": "Sábado"
}
print(f"Dia da semana correspondente: {A[numero]}")
