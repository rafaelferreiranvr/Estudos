"""Escreva um código que apresente a classe Televisor, com atributos ligado,
canal e volume e, o método imprimir. O método imprimir deve mostrar na tela os
valores de todos os atributos. O atributo ligado será booleano e deverá
indicar o estado atual do televisor, se ligado ou desligado. O atributo canal
deverá indicar o canal atual em que o televisor está sintonizado. O atributo
volume deverá indicar o volume atual do televisor. Adicione um método
construtor que permita a definição de todos os atributos no momento da
instanciação do objeto.

Adicione os métodos ligar e desligar que deverão mudar o conteúdo do atributo
ligado conforme o caso.
Adicione os atributos numeroCanais e, volumeMaximo, onde numeroCanais indica o
número máximo de canais que o televisor pode sintonizar e volumeMaximo indica
qual o maior nível de volume possível.
Adicione os métodos canalAcima e canalAbaixo, sendo que o método canalAcima
deve sintonizar sempre o próximo canal em relação ao canal atual, onde ao
chegar ao maior canal possível deverá voltar ao canal 1. O método canalAbaixo
deve sintonizar sempre o canal anterior em relação ao canal atual, onde ao
chegar ao canal 1 deverá voltar ao maior canal possível, simulando desta forma
o funcionamento de um televisor.

Adicione os métodos volumeAcima e volumeAbaixo, sendo que o método volumeAcima
deve modificar o volume para o próximo nível de volume possível, onde ao
chegar ao volumeMaximo não poderá possibilitar que o volume seja alterado. O
método volumeAbaixo deve modificar o volume para o nível imediatamente
inferior de volume em relação ao volume atual, não podendo ser menor do que 0,
simulando desta forma o funcionamento de um televisor.
"""


class televisor:
    def __init__(self, ligado, volume, volumeMaximo, canal, numeroCanais):
        if ligado is True or ligado is False:
            self.ligado = ligado
        else:
            raise TypeError("O atributo ligado deve ter um valor booleano.")

        self.volume = int(volume)
        self.volumeMaximo = int(volumeMaximo)
        self.numeroCanais = int(numeroCanais)
        self.canal = int(canal)

    def ligar(self):
        self.ligado = True

    def desligar(self):
        self.ligado = False

    def canalAcima(self):
        if (self.canal + 1) <= self.numeroCanais:
            self.canal += 1
        else:
            self.canal = 1

    def canalAbaixo(self):
        if (self.canal - 1) >= 1:
            self.canal -= 1
        else:
            self.canal = self.numeroCanais

    def volumeAcima(self):
        if (self.volume + 1) <= self.volumeMaximo:
            self.volume += 1

    def volumeAbaixo(self):
        if (self.volume - 1) >= 0:
            self.volume -= 1

    def imprimir(self):
        if self.ligado is True:
            self.ligado = "Ligada"
        else:
            self.ligado = "Desligada"

        dados = f"""Estado:{self.ligado}
Volume: {self.volume}
Volume Máximo: {self.volumeMaximo}
Canal: {self.canal}
Número de Canais: {self.numeroCanais}"""

        print(dados)


# Testes
t1 = televisor(True, 8, 10, 8, 10)
t1.canalAcima()
t1.canalAcima()
t1.canalAcima()
t1.volumeAcima()
t1.volumeAcima()
t1.volumeAcima()
t1.imprimir()
