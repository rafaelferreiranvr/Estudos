Algoritmo "maior_posicao"

Var
x, i, posicao : inteiro
n, maior: real


Inicio
escreva ("Quanto numeros voce vai digitar? ")
leia (x)

posicao <- 0
maior <- 0

para i de 0 ate (x-1) faca
   escreva ("Digite um numero: ")
   leia (n)
   
   se n > maior entao
   maior <- n
   posicao <- i
   fimse
fimpara

escreval ("Maior valor = ", maior:4:2)
escreva ("Posição do maior valor = ", posicao)



Fimalgoritmo