Algoritmo "bhaskara"

Var
a, b, c, raiz1, raiz2, delta : real

Inicio
escreva ("Coeficiente a: ")
leia (a)
escreva ("Coeficiente b: ")
leia (b)
escreva ("Coeficiente c: ")
leia (c)


delta <- exp (b, 2) - 4 * a * c

se delta < 0 entao
   escreva ("Essa equacao nao possui raizes reais.")
senao
   raiz1 <- (raizq (delta) - b) / 2 * a
   raiz2 <- (-1* (raizq (delta)) - b) / 2 * a
   escreval ("Raiz 1= ", raiz1)
   escreva ("Raiz 2= ", raiz2)
fimse


Fimalgoritmo