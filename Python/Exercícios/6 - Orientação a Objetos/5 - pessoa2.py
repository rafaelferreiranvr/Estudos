"""Escreva um código que apresente a classe Pessoa, com atributos nome,
endereço e telefone e, o método imprimir. O método imprimir deve mostrar na
tela os valores de todos os atributos. Adicione um método construtor que
permita a definição de todos os atributos no momento da instanciação do objeto.
"""


class pessoa:
    def __init__(self, nome, endereco, telefone):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone

    def imprimir(self):
        dados = f"""Nome: {self.nome}\nEndereço: {self.endereco}
Telefone: {self.telefone}"""
        print(dados)


# Testes (Dados gerados pelo 4devs.com.br)
p1 = pessoa("Helena Bastos", "Rua Bandeirantes, 1000, Azaré-SP", "99986-4417)")
p1.imprimir()
