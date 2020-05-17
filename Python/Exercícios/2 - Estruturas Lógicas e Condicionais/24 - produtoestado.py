"""Uma empresa vende o mesmo produto para quatro diferentes estados. 
Cada estado possui uma taxa diferente de imposto sobre o produto (MG 7%: SP 12%: RJ 15%: MS 8%). 
Faça um programa em que o usuário entre com o valor e o estado destino do produto
e o programa retorne o preço final do produto acrescido do imposto do estado em que ele será vendido.
Se o estado digitado não for válido, mostrar uma mensagem de erro. """
valor = float(input("Digite o valor do produto: "))
estado = input("Digite o estado(sigla): ")
taxas = {
    "MG": 107/100,
    "SP": 112/100,
    "RJ": 115/100,
    "MS": 108/100
}
if estado in taxas:
    print(f"Valor final do produto: {valor*taxas[estado]}")
else:
    print("Estado inválido.")
