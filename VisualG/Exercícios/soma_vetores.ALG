Algoritmo "soma_vetores"

Var
x, i, n : inteiro
a, b, c : vetor[0..9] de inteiro


Inicio
escreva ("Quantos valores vão ter cada vetor?: ")
leia (x)

escreval ("Digite os valores do vetor A: ")
para i de 0 ate x-1 faca
   leia (n)
   a[i] <- n
fimpara

escreval ("Digite os valores do vetor B: ")
para i de 0 ate x-1 faca
   leia (n)
   b[i] <- n
fimpara

para i de 0 ate x-1 faca
 c[i] <- a[i] + b[i]
 fimpara

escreval ("VETOR RESULTANTE: ")
para i de 0 ate x-1 faca
escreval (c[i])
fimpara


Fimalgoritmo