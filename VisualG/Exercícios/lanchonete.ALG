Algoritmo "lanchonete"

Var
codigo, quantidade : inteiro
preco, pagamento : real

Inicio
escreva ("Código do produto comprado: ")
leia (codigo)

escolha codigo

caso 1
preco <- 5

caso 2
preco <- 3.5

caso 3
preco <- 4.8

caso 4
preco <- 8.9

caso 5
preco <- 7.32

outrocaso
escreval ("Código de produto inválido ")
fimalgoritmo

fimescolha

escreva ("Quantidade comprada: ")
leia (quantidade)

pagamento <- quantidade * preco

escreva ("Valor a pagar: R$", pagamento:4:2)

Fimalgoritmo