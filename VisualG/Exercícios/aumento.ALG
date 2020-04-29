Algoritmo "aumento"

Var
salario, salarionovo, aumento, porcentagem : real

Inicio
escreva ("Digite o salario da pessoa: ")
leia (salario)

se (salario <= 1000) entao
salarionovo <- salario*1.2
senao
   se (salario <= 3000) entao
   salarionovo <- salario*1.15
   senao
     se (salario <= 8000) entao
     salarionovo <- salario*1.1
      senao
      salarionovo <- salario*1.05
     fimse
   fimse
fimse

aumento <- salarionovo - salario
porcentagem <- aumento * 100 / salario

escreval ("Novo salario: ", salarionovo:4:2)
escreval ("Aumento: ", aumento:4:2)
escreva ("Porcentagem: ", porcentagem, "%")

Fimalgoritmo