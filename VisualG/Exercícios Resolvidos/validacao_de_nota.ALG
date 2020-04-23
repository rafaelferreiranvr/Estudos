Algoritmo "validacao_de_nota"

Var
A, B, media : real
Inicio

escreva ("Digite a primeira nota: ")
leia (A)

enquanto (A<0) ou (A>10) faca
escreval ("Valor invalido! Tente novamente: ")
leia (A)
fimenquanto

escreva ("Digite a segunda nota: ")
leia (B)

enquanto (B<0) ou (B>10) faca
escreval ("Valor invalido! Tente novamente: ")
leia (B)
fimenquanto

media <- (A + B)/2

escreval ("Média: ", media)


Fimalgoritmo