Algoritmo "aprovados"

Var
nome : vetor[0..9] de caractere
sem1, sem2 : vetor[0..9] de real
x, i : inteiro
Inicio
escreva ("Quantos alunos serão digitados? ")
leia (x)

para i de 0 ate x-1 faca
   escreval ("Digite nome, primeira e segunda nota do ", (i+1), "o aluno: ")
   leia (nome[i])
   leia (sem1[i])
   leia (sem2[i])
fimpara

escreval ("Alunos aprovados: ")
para i de 0 ate x-1 faca
   se ((sem1[i] + sem2[i])/2 >= 6) entao
   escreval (nome[i])
   fimse
fimpara

Fimalgoritmo