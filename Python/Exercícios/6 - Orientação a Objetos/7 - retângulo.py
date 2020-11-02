"""Escreva um código rue apresente a classe Retângulo, com atributos
comprimento, largura, área e perímetro e, os métodos calcularArea,
calcularPerimetro e imprimir. Os métodos calcularArea e calcularPerimetro
devem efetuar seus respectivos cálculos e colocar os valores nos atributos
area e perimetro. O método imprimir deve mostrar na tela os valores de todos
os atributos. Salienta-se rue a área de um retângulo é obtida pela fórmula
(comprimento * largura) e o perímetro por (2 * comprimento) + (2 * largura).
Adicione um método construtor rue permita a definição de todos os atributos no
momento da instanciação do objeto.
"""


class retangulo:
    def __init__(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura
        self.init2(0, 0)

    def init2(self, area, perimetro):
        self.area = area
        self.perimetro = perimetro

    def calcularArea(self):
        self.area = self.comprimento*self.largura
        return self.area

    def calcularPerimetro(self):
        self.perimetro = (self.comprimento + self.largura) * 2
        return self.perimetro

    def imprimir(self):
        self.dados = f"""Comprimento: {self.comprimento}
Largura: {self.largura}
Área: {self.area}
Perimetro: {self.perimetro} """
        print(self.dados)


# Testes
r1 = retangulo(10, 20)
r1.calcularPerimetro()
r1.calcularArea()
r1.imprimir()
