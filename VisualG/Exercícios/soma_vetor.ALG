Algoritmo "soma_vetor"

Var
n, soma, media : real
i, x : inteiro
vet : vetor [0..9] de real

Inicio

escreva ("Quantos numeros voce vai digitar? ")
leia (x)

soma <- 0

para i de 0 ate x-1 faca
   escreva ("Digite um numero: ")
   leia (n)
   vet[i] <- n
   soma <- soma + n
fimpara

media <- soma/x

escreva ("Valores: ")
para i de 0 ate x-1 faca
   escreva (vet[i]:6:2, " ")
fimpara
escreval
escreval ("Soma: ", soma)
escreva ("Media: ", media)

Fimalgoritmo