"""Escreva um código que apresente a classe Quadrado, com atributos lado, área
e perímetro e, os métodos calcularArea, calcularPerimetro e imprimir.
Os métodos calcularArea e calcularPerimetro devem efetuar seus respectivos
cálculos e colocar os valores nos atributos area e perimetro.
O método imprimir deve mostrar na tela os valores de todos os atributos.
Salienta-se que a área de um quadrado é obtida pela fórmula (lado * lado)
e o perímetro por (4 * lado). Adicione um método construtor que permita a
definição de todos os atributos no momento da instanciação do objeto.
"""


class quadrado:
    def __init__(self, lado):
        self.lado = lado
        self.init2(0, 0)

    def init2(self, perimetro, area):
        self.perimetro = perimetro
        self.area = area

    def calcularArea(self):
        self.area = self.lado**2
        return self.area

    def calcularPerimetro(self):
        self.perimetro = self.lado*4
        return self.perimetro

    def imprimir(self):
        self.dados = f"""Lado: {self.lado} \nÁrea: {self.area}
Perimetro: {self.perimetro} """
        print(self.dados)


# Testes
q1 = quadrado(10)
q1.calcularPerimetro()
q1.calcularArea()
q1.imprimir()
