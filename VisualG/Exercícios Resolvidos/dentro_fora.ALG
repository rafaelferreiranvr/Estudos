Algoritmo "dentro_fora"

Var
x, i, dentro, fora: inteiro
Inicio
escreval ("Quantos numeros voce vai digitar? ")
leia (x)



dentro <- 0
fora <- 0
para i de 1 ate x faca
   escreva ("Digite um número: ")
   leia (i)
   se (i >= 10) e (i <= 20) entao
      dentro <- dentro + 1
   senao
      fora <- fora + 1
   fimse
fimpara

escreval (dentro, " dentro")
escreva (fora, " fora")



Fimalgoritmo