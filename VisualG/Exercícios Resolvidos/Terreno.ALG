Algoritmo "terreno"

Var
 larg, comp, valor, area, preco : real



inicio
   
   escreval ("Digite a largura do terreno: ")
   leia (larg)
   escreval ("Digite o comprimento do terreno:  ")
   leia (comp)
   escreval ("Digite o valor do metro quadrado: ")
   leia (valor)
   area <- larg * comp
   preco <- area * valor
   escreval ("Area do terreno = ", area:8:2)
   escreval ("Preco do terreno = ", preco:8:2)


Fimalgoritmo