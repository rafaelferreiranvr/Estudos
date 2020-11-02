"""Escreva um código que apresente a classe Moto, com atributos marca, modelo,
cor e marcha e, o método imprimir. O método imprimir deve mostrar na tela os
valores de todos os atributos. O atributo marcha indica em que a marcha a Moto
se encontra no momento, sendo representado de forma inteira, onde:
0 neutro, 1 — primeira, 2 — segunda, etc.


Adicione os métodos marchaAcima e marchaAbaixo que deverão efetuar a troca de
marchas, onde o método marchaAcima deverá subir uma marcha, ou seja, se a moto
estiver em primeira marcha, deverá ser trocada para segunda marcha e assim por
diante. O método marchaAbaixo deverá realizar o oposto, ou seja, descer a
marcha.

Adicione os atributos menorMarcha e maiorMarcha, onde o atributo menorMarcha
indica qual será a menor marcha possível para a moto e o atributo maiorMarcha
indica qual será a maior marcha possível. Desta forma os métodos marchaAcima e
marchaAbaixo devem ser reescritos de forma a não permitirem a troca de marchas
para valores abaixo da menorMarcha e acima da maiorMarcha.

Adicione o atributo ligada que terá a função de indicar se a moto está ligada
ou não. Este atributo deverá ser do tipo booleano.
Adicione os métodos ligar e desligar que deverão mudar o conteúdo do atributo
ligada conforme o caso.

Adicione um método construtor que permita a definição de todos os atributos no
momento da instanciação do objeto.
"""


class moto:
    def __init__(self, modelo, cor, marcha, menorMarcha, maiorMarcha, ligada):
        self.modelo = str(modelo)
        self.cor = str(cor)
        self.ligada = ligada
        if menorMarcha < maiorMarcha:
            self.menorMarcha = int(menorMarcha)
            self.maiorMarcha = int(maiorMarcha)
        else:
            raise IndexError("Valor da marcha fora do intervalo especificado.")

        if menorMarcha <= marcha <= maiorMarcha:
            self.marcha = int(marcha)
        else:
            raise IndexError("Valor da marcha fora do intervalo especificado.")

        if self.ligada is True or self.ligada is False:
            self.ligada = ligada
        else:
            raise ValueError("Valor do atributo ligado deve ser booleano.")

    def marchaAcima(self):
        if self.menorMarcha <= (self.marcha + 1) <= self.maiorMarcha:
            self.marcha += 1
        else:
            print("Valor da marcha fora do intervalo especificado.")

    def marchaAbaixo(self):
        if self.menorMarcha <= (self.marcha - 1) <= self.maiorMarcha:
            self.marcha -= 1
        else:
            print("Valor da marcha fora do intervalo especificado.")

    def ligar(self):
        self.ligada = True

    def desligar(self):
        self.ligada = False

    def imprimir(self):
        if self.ligada:
            self.ligada = "Ligada"
        else:
            self.ligada = "Desligada"

        dados = f"""Modelo: {self.modelo}
Cor: {self.cor}
Marcha: {self.marcha}
Menor Marcha: {self.menorMarcha}
Maior Marcha: {self.maiorMarcha}
Estado: {self.ligada}
"""
        print(dados)


# Testes
m1 = moto("Ducati 1198", "Vermelha", 0, 0, 6, True)
m1.marchaAcima()
m1.marchaAcima()
m1.marchaAcima()
m1.marchaAbaixo()
m1.marchaAbaixo()
m1.imprimir()
