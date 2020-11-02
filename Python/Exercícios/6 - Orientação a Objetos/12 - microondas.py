"""Escreva um código que apresente a classe Microondas, com atributo ligado e
o método imprimir. O método imprimir deve mostrar na tela os valores de todos
os atributos. O atributo ligado será booleano e deverá indicar o estado atual
do microondas, se ligado ou desligado.
Adicione um método construtor que permita a definição de todos os atributos no
momento da instanciação do objeto. Adicione os métodos ligar e desligar que
deverão mudar o conteúdo do atributo ligado conforme o caso.
Adicione o atributo portaFechada que deverá ser booleano e deverá indicar se a
porta do microondas está ou não fechada. O método imprimir deve ser modificado
de forma a mostrar na tela os valores de todos os atributos.
Adicione os métodos fecharPorta e abrirPorta que deverá mudar o conteúdo do
atributo portaFechada conforme o caso.
Modifique o método ligar para que só ligue o equipamento quando a porta do
mesmo estiver fechada, simulando assim o funcionamento de um microondas.
"""


class microondas:
    def __init__(self, ligado, portaFechada):
        if (ligado is True or ligado is False) and (portaFechada is True or
                                                    portaFechada is False):
            self.ligado = ligado
            self.portaFechada = portaFechada
        else:
            mensagem = "Os atributos 'ligado' e 'portaFechada' são booleanos."
            raise TypeError(mensagem)

    def ligar(self):
        if self.fecharPorta is True:
            self.ligado = True
        else:
            print("""O Microondas deve estar com a porta fechada para ser
ligado""")

    def desligar(self):
        self.ligado = False

    def abrirPorta(self):
        self.portaFechada = False

    def fecharPorta(self):
        self.portaFechada = True

    def imprimir(self):
        if self.portaFechada is True:
            self.portaFechada = "Fechada"
        else:
            self.portaFechada = "Aberta"

        if self.ligado is True:
            self.ligado = "Ligado"
        else:
            self.ligado = "Desligado"

        dados = f"""Porta: {self.portaFechada}
Estado: {self.ligado}"""
        print(dados)


# Testes
m1 = microondas(True, True)
m1.abrirPorta()
m1.fecharPorta()
m1.ligar()
m1.imprimir()
