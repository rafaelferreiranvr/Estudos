"""Faca uma funcao que receba a data atual (dia, mes e ano em inteiro) e exiba-a na tela no formato textual por extenso. 
Exemplo: Data: 01/01/2000, Imprimir: 1 de janeiro de 2000. 
"""
n = input("Digite a data no seguinte formato DD/MM/AAAA: ")

def extenso(x):
    m = x.split("/")
    if (int(m[0]) > 31) or (int(m[0]) > 29 and int(m[1]) == 2) or ((int(m[0]) <= 0) or (int(m[1]) <= 0) or (int(m[2]) <= 0)):
        raise IndexError("Data inválida.")
    mes = {
        1 : "Janeiro",
        2 : "Fevereiro",
        3 : "Março",
        4 : "Abril",
        5 : "Maio",
        6 : "Junho",
        7 : "Julho",
        8 : "Agosto",
        9 : "Setembro", 
        10 : "Outubro",
        11 : "Novembro",
        12 : "Dezembro"
    }
    return f"{m[0]} de {mes[int(m[1])]} de {m[2]}"
print(extenso(n))