Algoritmo "temperatura"

Var
f, c : real
escala : caractere
Inicio
escreval ("Voce vai digitar a temperatura em qual escala (C/F)? ")
leia (escala)

se escala = "F" entao
 escreva ("Digite a temperatura em Fahrenheit: ")
 leia (f)
 c <- 5/9 * (f - 32)
 escreva ("Temperatura equivalente em celsius: ", c:4:2)

senao
  se escala = "C" entao
    escreva ("Digite a temperatura em Celsius: ")
    leia (c)
    f <- 9*c/5 + 32
    escreva ("Temperatura equivalente em Fahrenheit: ", f:4:2)

  fimse
fimse
Fimalgoritmo