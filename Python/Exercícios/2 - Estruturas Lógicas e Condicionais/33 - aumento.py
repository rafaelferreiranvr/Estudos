"""Um produto vai sofrer aumento de acordo com a tabela abaixo. Leia o preço antigo. calcule e escreva o preço novo. e escreva uma mensagem em função do preço novo (de acordo com a segunda tabela). 
PREÇO ANTIGO      PERCENTUAL DE AUMENTO 
até R$ 50                  5% 
entre R$ 50 e R$ 100       10% 
acima de R$ 100            15%


PREÇO NOVO                              MENSAGEM 
até R$ 80                                Barato 
entre R$ 80 e R$ 120 (inclusive)         Normal 
entre R$ 120 e R$ 200 (inclusive)         Caro 
acima de R$ 200                        Muito caro 
"""

preco = float(input("Digite o preço antigo: "))
aumento = 0
mensagem = " "
if preco < 50:
    aumento = 1.05
elif 50 <= preco <= 100:
    aumento = 1.10
else:
    aumento = 1.15

preco *= aumento

if preco <= 80:
    print("Barato")
elif 80 < preco <= 120:
    print("Normal")
elif 120 < preco <=200:
    print("Caro") 
else:
    print("Muito caro")
    
print(f"Valor: {preco}")