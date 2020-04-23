Algoritmo "diagonal_negativos"

Var
m, i, j, neg : inteiro
mat : vetor [0..4, 0..4] de inteiro

Inicio
escreva ("Qual a ordem da matriz? ")
leia (m)

neg <- 0

para i de 0 ate m-1 faca
   para j de 0 ate m-1 faca
      escreva ("Elemento [", i, ",", j, "]: ")
      leia (mat[i, j])
      se mat[i, j] < 0 entao
      neg <- neg + 1
      fimse
   fimpara
fimpara

escreva ("Diagonal principal: ")
para i de 0 ate m-1 faca
   para j de 0 ate m-1 faca
   se i = j entao
   escreva (mat[i,j])
   fimse
   fimpara
fimpara

escreval
escreva ("Quantidade de negativos = ", neg)


Fimalgoritmo