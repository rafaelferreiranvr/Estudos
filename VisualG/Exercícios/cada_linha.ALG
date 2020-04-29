Algoritmo "cada_linha"

Var
m, i, j : inteiro
maior : vetor [0..9] de inteiro
mat : vetor [0..9, 0..9] de inteiro

Inicio
escreva ("Qual a ordem da matriz? ")
leia (m)

para i de 0 ate m-1 faca
   para j de 0 ate m-1 faca
      escreva ("Elemento [", i, ",", j, "]: ")
      leia (mat[i, j])
      se mat[i, j] > maior[i] entao
         maior[i] <- mat [i, j]
      fimse
   fimpara
fimpara

escreval ("Maior elemento de cada linha: ")
para i de 0 ate m-1 faca
   escreval (maior[i])
fimpara



Fimalgoritmo