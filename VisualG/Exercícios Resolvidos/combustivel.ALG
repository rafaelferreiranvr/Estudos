Algoritmo "combustivel"


Var
alc, gas, diesel, digitado : inteiro

Inicio

escreval ("Informe um codigo (1, 2, 3) ou 4 para parar: ")
leia (digitado)

alc <- 0
gas <- 0
diesel <- 0

enquanto digitado <> 4 faca

escolha digitado
   caso 1
   alc <- alc + 1

   caso 2
   gas <- gas + 1
   
   caso 3
   diesel <- diesel + 1

fimescolha

escreval ("Informe um codigo (1, 2, 3) ou 4 para parar: ")
leia (digitado)

fimenquanto

escreval ("MUITO OBRIGADO")
   escreval ("Alcool: ", alc)
   escreval ("Gasolina: ", gas)
   escreval ("Diesel: ", diesel)

Fimalgoritmo