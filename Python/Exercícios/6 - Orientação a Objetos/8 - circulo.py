"""Escreva um código que apresente a classe Circulo, com atributos raio, área
e perímetro e, os métodos calcularArea, calcularPerimetro e imprimir.
Os métodos calcularArea e calcularPerimetro devem efetuar seus respectivos
cálculos e colocar os valores nos atributos area e perimetro.
O método imprimir deve mostrar na tela os valores de todos os atributos.
Salienta-se que a área de um círculo é obtida pela fórmula (pi * raio * raio) e
o perímetro por (2 * pi * raio), onde pi = 3,141516.
Adicione um método construtor que permita a definição de todos os atributos no
momento de instanciação do objeto.
"""


class circulo:
    def __init__(self, raio):
        self.raio = raio
        self.init2(0, 0)

    def init2(self, area, perimetro):
        self.area = area
        self.perimetro = perimetro

    def calcularArea(self):
        self.area = (self.raio**2) * 3.141516

    def calcularPerimetro(self):
        self.perimetro = 2 * 3.141516 * self.raio

    def imprimir(self):
        dados = f"""Raio: {self.raio}
Área: {self.area}
Perímetro: {self.perimetro}
"""
        print(dados)


# Testes
c1 = circulo(5)
c1.calcularArea()
c1.calcularPerimetro()
c1.imprimir()
