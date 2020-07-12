"""Faça um algoritmo que calcule o IMC de uma pessoa e mostre sua classificação de acordo com a tabela abaixo: 
IMC                    Classificação 
18,5                   Abaixo do Peso 
18,6 - 24,9              Saudável 
25,0 - 29,9           Peso em excesso 
30,0 - 34,9           Obesidade Grau I 
35,0 - 39,9       Obesidade Grau II(severa) 
40,0 Obesidade Grau III(mórbida) """

altura = float(input("Digite a altura: "))
peso = float(input("Digite o peso: "))
imc = peso/(altura**2) 

classificacao = {
    imc <= 18.5 : "Abaixo do peso",
    18.5 < imc <= 25 : "Saudável",
    25 < imc <= 30 : "Peso em excesso",
    30 < imc <= 35 : "Obesidade Grau I",
    35 < imc <= 40 : "Obesidade Grau II(severa)",
    imc > 40 : "Obesidade Grau 3(mórbida)"
}

print(f"IMC: {imc} \nClassificação: {classificacao[True]}")