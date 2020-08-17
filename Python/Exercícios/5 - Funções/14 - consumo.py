"""Faça uma função que receba a distância em Km e a quantidade de litros de
gasolina consumidos por um carro em um percurso.
Calcule o consumo em Km/l e escreva uma mensagem de acordo com a tabela abaixo:
CONSUMO (Km/l)        MENSAGEM
menor que 8           Venda o carro!
entre 8 e 12          Econômico!
maior que 12          Super econômico! """

k = float(input("Digite a distância percorrida em km: "))
litros = float(input("Digite os litros de gasolina consumidos: "))


def consumo(km, lt):
    c = km / lt
    op = {
        c < 8: "Venda o carro!",
        8 <= c <= 12: "Econômico!",
        c > 12: "Super econômico"
    }
    return op[True]


print(consumo(k, litros))
