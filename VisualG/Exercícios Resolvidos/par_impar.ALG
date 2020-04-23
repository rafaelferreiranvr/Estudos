Algoritmo "par_impar"

Var
x, n, i : inteiro
a, b : caractere


Inicio
escreva ("Quantos números você vai digitar? " )
leia (x)

para i de 1 ate x faca
   escreva ("Digite um numero: ")
   leia (n)
   se  (n > 0) entao
       a <- "POSITIVO "
   senao
      se (n < 0) entao
        a <- "NEGATIVO "
      senao
        a <- "NULO"
      fimse
   fimse
   
   se (n % 2 = 0) entao
      b <- "PAR"
   senao
      b <- "IMPAR"
   fimse
      
   se n = 0 entao
     escreval (a)
   senao
     escreval (a, b)
   fimse
fimpara

Fimalgoritmo