Algoritmo "retangulo"

Var
   base, altura, perimetro, diagonal,area : real


Inicio
   escreval ("Base do retangulo: ")
   leia (base)
   escreval ("Altura do retângulo: ")
   leia (altura)

   area <- base * altura
   perimetro <- 2 * (base + altura)
   diagonal <- raizq(quad(base) + quad(altura))
   
   escreval ("AREA = ", area)
   escreval ("PERIMETRO = ", perimetro:1:2)
   escreval ("DIAGONAL = ", diagonal:1:5)


Fimalgoritmo