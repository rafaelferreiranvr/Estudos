Algoritmo "dardo"

Var
da, db, dc, maior : real



Inicio
escreval ("Digite as tres distancias: ")
leia (da)
leia (db)
leia (dc)

se (da > db) e (da > dc) entao
maior <- da
  senao
    se db > dc entao
    maior <- db
    senao
    maior <- dc
  fimse
fimse

escreva ("MAIOR DISTANCIA ", maior:4:2)



Fimalgoritmo