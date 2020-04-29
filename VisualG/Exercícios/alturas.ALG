Algoritmo "alturas"

Var
idade, x, i : inteiro
nome : caractere
media, soma, altura, porcentagem, menores : real
vet : vetor [0..9] de caractere

Inicio
escreva ("Quantas pessoas serão digitadas? ")
leia (x)

soma <- 0
menores <- 0

para i de 0 ate x-1 faca
   escreval ("Dados da ", (i+1), "a pessoa:")
   escreva ("Nome: ")
   leia (nome)
   escreva ("Idade: ")
   leia (idade)
   escreva ("Altura: ")
   leia (altura)
   
   soma <- soma + altura
   
   se (idade < 16) entao
      vet[i] <- nome
      menores <- menores + 1
   fimse
fimpara

porcentagem <- menores * 100 / x

escreval
escreval ("Altura média: ", soma/x)
escreval ("Pessoas com menos de 16 anos: ", porcentagem, "%")

para i de 0 ate x-1 faca
   se vet[i] <> "" entao
   escreval (vet[i])
   fimse
fimpara


   
   



Fimalgoritmo