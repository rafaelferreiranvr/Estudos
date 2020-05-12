''' A importância de R$ 780.000,00 será dividida entre trés ganhadores de um concurso. Sendo que da quantia total: 
O primeiro ganhador receberá 46%
O segundo receberá 32%; 
O terceiro receberá o restante
Calcule e imprima a quantia ganha por cada um dos ganhadores. 
''' 
valor = 780000
ganhador1 = valor * 0.46
ganhador2 = valor * 0.32
ganhador3 = valor - (ganhador1 + ganhador2)
print(f"O primeiro, o segundo e o terceiro ganhador receberão {ganhador1}, {ganhador2} e {ganhador3}, respectivamente.")