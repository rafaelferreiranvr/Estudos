Algoritmo "operadora"

Var
minutos, valor : inteiro

Inicio
escreval ("Digite a quantidade de minutos: ")
leia (minutos)

se minutos < 100 entao
   valor <- 50
senao
  se minutos > 100 entao
  valor <- 50 + (minutos - 100) * 2
  fimse
fimse

escreva ("Valor a pagar: R$ ", valor)
Fimalgoritmo