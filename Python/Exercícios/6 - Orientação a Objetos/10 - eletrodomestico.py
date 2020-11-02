"""Escreva um código que apresente a classe Eletrodoméstico, com atributo
ligado e o método imprimir. O método imprimir deve mostrar na tela os valores
de todos os atributos. O atributo ligado será booleano e deverá indicar o
estado atual do eletrodoméstico, se ligado ou desligado.
Adicione os métodos ligar e desligar que deverão mudar o conteúdo do atributo
ligado conforme o caso.
Adicione um método construtor que permita a definição de todos os atributos no
momento da instanciação do objeto.
"""


class eletrodomestico:
    def __init__(self, ligado):
        if ligado is True or ligado is False:
            self.ligado = ligado
        else:
            raise TypeError("O atributo ligado deve ser booleano. ")

    def ligar(self):
        self.ligado = True

    def desligar(self):
        self.ligado = False

    def imprimir(self):
        if self.ligado is True:
            self.ligado = "Ligado."
        else:
            self.ligado = "Desligado."
        print(F"Estado: {self.ligado}")


# Testes
e1 = eletrodomestico(True)
e1.desligar()
e1.ligar()
e1.imprimir()
