Algoritmo "divisao"

Var
x, i : inteiro
divisao, d, n : real


Inicio
escreva ("Quantos casos você vai digitar? ")
leia (x)

para i de 1 ate x faca
   escreva ("Entre com o numerador: ")
   leia (n)
   escreva ("Entre com o denominador: ")
   leia (d)
   se d = 0 entao
      escreval ("Divisão impossível")
   senao
      divisao <- n/d
      escreval ("Divisão = ", divisao:4:2)
   fimse
fimpara
Fimalgoritmo