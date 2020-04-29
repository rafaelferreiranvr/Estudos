Algoritmo "troco"

Var
uni, recebido, troco : real
quantidade : inteiro

Inicio
escreva ("Preço unitário do produto: ")
leia (uni)
escreva ("Quantidade comprada: ")
leia (quantidade)
escreva ("Dinheiro recebido: ")
leia (recebido)
troco <- recebido - uni * quantidade
escreva ("TROCO= ", troco)


Fimalgoritmo