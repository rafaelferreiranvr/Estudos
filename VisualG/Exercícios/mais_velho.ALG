Algoritmo "mais_velho"


Var
x, i, maioridade : inteiro
maiornome : caractere
nome : vetor[0..9] de caractere
idade : vetor [0..9] de inteiro


Inicio
escreva ("Quantas pessoas você vai digitar? ")
leia (x)

maioridade <- 0

para i de 0 ate x-1 faca
   escreval ("Dados da ", (i+1), "a pessoa:")
   escreva ("Nome: ")
   leia (nome[i])
   escreva ("Idade: ")
   leia (idade[i])
   se idade [i] > maioridade entao
      maioridade <- idade[i]
      maiornome <- nome[i]
   fimse
fimpara

escreva ("Pessoa mais velha: ", maiornome)

Fimalgoritmo