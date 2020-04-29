Algoritmo "fatorial"

Var
n, i, fatorial : inteiro

Inicio

escreva ("Digite o valor de N: ")
leia (n)

i <- 1

  se (n = 0) ou (n = 1) entao
        fatorial <- 1
   senao
      fatorial <- n
      para i de 1 ate (n-1) faca
         fatorial <- fatorial * (n - i)
      fimpara
   fimse

escreva ("FATORIAL = ", fatorial)

Fimalgoritmo