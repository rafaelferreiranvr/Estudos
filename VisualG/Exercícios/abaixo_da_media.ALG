Algoritmo "abaixo_da_media"

Var
x, n, i : inteiro
vet : vetor[0..9] de real
media, soma : real
Inicio
escreva ("Quantos elementos vai ter o vetor? ")
leia (x)

soma <- 0
i <- 0

para i de 0 ate x-1 faca
   escreva ("Digite um numero: ")
   leia (vet[i])
   soma <- soma + vet[i]
fimpara
   
media <- soma/x

escreval ("MEDIA DO VETOR = ", media:6:3)
escreval ("Elementos abaixo da media: ")
para i de 0 ate x-1 faca
   se vet[i] < media entao
    escreval (vet[i])
   fimse
fimpara

   


Fimalgoritmo