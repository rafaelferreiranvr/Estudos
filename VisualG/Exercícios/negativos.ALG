Algoritmo "negativos"

Var
x, n, i : inteiro
vet : vetor [0..9] de inteiro

Inicio

escreva ("Quantos números você vai digitar? ")
leia (x)

para i de 0 ate x-1 faca
  escreva ("Digite um numero: ")
  leia (n)
  vet[i] <- n
fimpara

escreval ("Numeros Negativos: ")

para i de 0 ate x-1 faca
 se vet[i] < 0 entao
  escreval (vet[i])
 fimse
fimpara

Fimalgoritmo