Algoritmo "media_pares"


Var
pares, somapares, x, i, n : inteiro
media : real
vet : vetor [0..9] de inteiro

Inicio
escreva ("Quantos elementos vai ter o vetor? ")
leia (x)

para i de 0 ate x-1 faca
   escreva ("Digite um numero: ")
   leia (vet[i])
   se vet[i] % 2 = 0 entao
      pares <- pares + 1
      somapares <- somapares + vet[i]
   fimse
fimpara

se pares <> 0 entao
   media <- somapares/pares
   escreva ("MEDIA DOS PARES = ", media)
senao
   escreva ("NENHUM NUMERO PAR")
fimse

Fimalgoritmo