Algoritmo "experiencias"

Var
c, r, s, total, pc, pr, ps, parcial : real
t : caractere
i, casos : inteiro
Inicio

escreva ("Quantos casos de teste serao digitados? ")
leia (casos)

c <- 0
r <- 0
s <- 0

parcial <- 0

para i de 1 ate casos faca
   escreva ("Quantidade de cobaias: ")
   leia (parcial)
   escreva ("Tipo de cobaias: ")
   leia (t)
   
   escolha t
     caso "C"
       c <- c + parcial
     caso "R"
       r <- r + parcial
     caso "S"
       s <- s + parcial
     fimescolha
  total <- total + parcial
fimpara

pc <- c*100/total
pr <- r*100/total
ps <- s*100/total

escreval ("Relatorio Final: ")
escreval ("Total: ", total)
escreval ("Total de coelhos: ", c)
escreval ("Total de ratos: ", s)
escreval ("Total de sapos: ", r)
escreval ("Percentual de coelhos: ", pc:4:2)
escreval ("Percentual de ratos: ", pr:4:2)
escreval ("Percentual de sapos: ", ps:4:2)

Fimalgoritmo