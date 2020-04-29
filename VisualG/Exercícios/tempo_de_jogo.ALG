Algoritmo "tempo_de_jogo"

Var
hi, hf, duracao : inteiro


Inicio
escreva ("Hora inicial: ")
leia (hi)
escreva ("Hora final: ")
leia (hf)

se hf > hi entao
   duracao <- hf - hi
   senao
   duracao <- 24 - (hi - hf)
fimse

escreva ("O JOGO DUROU ", duracao, " horas")




Fimalgoritmo