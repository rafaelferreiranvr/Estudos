Algoritmo "media_idades"

Var
n, quantidade, soma : inteiro
media : real

Inicio

escreval ("Digite as idades: ")
leia (n)

se n < 0 entao
escreva ("Impossível calcular")
fimalgoritmo
fimse


quantidade <- 0
soma <- 0

enquanto n > 0 faca
soma <- soma + n
quantidade <- quantidade + 1
leia (n)
fimenquanto

media <- soma / quantidade

escreval ("MEDIA: ", media:4:2)




Fimalgoritmo