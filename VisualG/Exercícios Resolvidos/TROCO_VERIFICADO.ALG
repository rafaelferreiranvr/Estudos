Algoritmo "troco_verificado"

Var
 puni, quantidade, drecebido, troco, falta, total : real
 
Inicio
 escreva ("Preço unitário do produto: ")
 leia (puni)
 escreva ("Quantidade comprada: ")
 leia (quantidade)
 escreva ("Dinheiro recebido: ")
 leia (drecebido)
 
 total <- puni * quantidade

 se drecebido < total entao
 falta <- total - drecebido
 escreva ("DINHEIRO INSUFICIENTE. FALTAM ", falta, " REAIS")
  senao
  troco <- drecebido - total
  escreva ("TROCO = ", troco:4:2)
 fimse


Fimalgoritmo