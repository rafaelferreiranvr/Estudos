Algoritmo "soma_impares"

Var
x, y, soma, i, a, b, c : inteiro


Inicio
escreval ("Digite dois números: ")
leia (x)
leia (y)

se x < y entao
   se x % 2 = 0 entao
     a <- 1
   senao
     a <- 2
   fimse
   
   se y % 2 = 0 entao
      b <- y - x - 1
   senao
      b <- y - x - 2
   fimse
   
   c <- 2
senao
   se x % 2 = 0 entao
     a <- -1
   senao
     a <- -2
   fimse
   
   se y % 2 = 0 entao
     b <- y + 1 - x
   senao
     b <- y + 2 - x
   fimse

   c <- -2
fimse

soma <- 0

para i de a ate b passo c faca
   soma <- soma + x + i
fimpara

escreval ("SOMA DOS IMPARES= ", soma)

Fimalgoritmo