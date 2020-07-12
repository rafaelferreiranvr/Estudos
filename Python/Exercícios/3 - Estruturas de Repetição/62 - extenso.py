"""Se os números de 1 a 5 são escritos em palavras: 
um, dois, três, quatro, cinco,
então há 2 + 4 + 4 + 6 + 5 = 22 letras usadas no total. 
Faça um programa que conte quantas letras seriam utilizadas se todos os números 
de 1 a 1000 (mil) fossem escritos em palavras. 
OBS: Não conte espaços ou hifens. """
menor19 = {
    1 : "um",
    2 : "dois",
    3 : "tres",
    4 : "quatro",
    5 : "cinco",
    6 : "seis",
    7 : "sete",
    8 : "oito",
    9 : "nove",
    10 : "dez",
    11 : "onze",
    12 : "doze",
    13 : "treze", 
    14 : "catorze",
    15 : "quinze",
    16 : "dezesseis",
    17 : "dezessete",
    18 : "dezoito",
    19 : "dezenove" 
}
dezena = {
    0 : "",
    2 : "vinte",
    3 : "trinta",
    4 : "quarenta",
    5 : "cinquenta",
    6 : "sessenta",
    7 : "setenta",
    8 : "oitenta", 
    9 : "noventa",
}
centena = {
    0 : "",
    1 : "cem",
    2 : "duzentos",
    3 : "trezentos", 
    4 : "quatrocentos",
    5 : "quinhentos", 
    6 : "seiscentos", 
    7 : "setecentos",
    8 : "oitocentos", 
    9 : "novecentos"
}
q = 0
p = ""
for x in range(1, 1001):
    if 1 <= x < 20:
        p = menor19[x]
    elif 20 <= x < 100:
        d = int(str(x)[0])
        u = int(str(x)[1])
        if u == 0:
            p = f"{dezena[d]}"
        else:
            p = f"{dezena[d]}e{menor19[u]}"
    elif 100 <= x < 1000:
        c = int(str(x)[0])
        d = int(str(x)[1])
        u = int(str(x)[2])
        w = int(f"{str(x)[1]}{str(x)[2]}")
        if c == 1:
            if d == 0 and u == 0:
                p = centena[c]
            elif 1 <= w <= 19:
                p = f"centoe{menor19[w]}"
            elif u == 0:
                p = f"centoe{dezena[d]}"
            else:
                p = f"centoe{dezena[d]}e{menor19[u]}"
        else:
            if d == 0 and u == 0:
                p = centena[c]
            elif 1 <= w <= 19:
                p = f"{centena[c]}e{menor19[w]}"
            elif u == 0:
                p = f"{centena[c]}e{dezena[d]}"
            else:
                p = f"{centena[c]}e{dezena[d]}e{menor19[u]}"
    elif x == 1000:
        p = "mil"
    q += len(p)
print(f"Número de letras: {q}")