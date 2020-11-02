"""Crie uma classe para representar uma pessoa, com os atributos privados de
nome, idade e altura.
Crie os métodos públicos necessários para sets e gets e também um método para
imprimir os dados de uma pessoa.
"""


class Pessoa:
    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura

    def setnome(self, nome):
        self.nome = nome

    def setidade(self, idade):
        self.idade = idade

    def setaltura(self, altura):
        self.altura = altura

    def getnome(self):
        print(self.nome)

    def getidade(self):
        print(self.idade)

    def getaltura(self):
        print(self.altura)

    def dados(self):
        valor = f"Nome: {self.nome}\nAltura:{self.altura}\nIdade: {self.idade}"
        print(valor)


# Testes
p = Pessoa("Henrique", 20, 1.70)
p.setnome("Renato")
p.setidade(22)
p.setaltura(1.82)
p.getnome()
p.getaltura()
p.getidade()
p.dados()
