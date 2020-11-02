"""Crie uma classe Equipamento com dois atributos privados.
Crie uma classe Computador com dois atributos à sua escolha, também privados.
A classe Computador deverá herdar tudo da classe Equipamento.
Crie os métodos de acesso e de modificação para todos os atributos definidos
em ambas as classes.
Crie uma classe TestaEquipamento, que deverá conter o método main(), crie nela
um objeto da classe Equipamento e instancie os dois atributos que você
declarou na classe Equipamento.
Crie também um objeto da classe Computador, utilizando os dois atributos
declarados na própria classe e os dois herdados da classe Equipamento.
O método main() deve exibir as informações dos dois objetos criados.
Criar o método exibe() na classe Equipamento para mostrar os dados dessa
classe.
Reescreva o método exibe() na classe Computador, aproveitando o que já está
escrito na superclasse Equipamento.
"""


class equipamento:
    def __init__(self, preco, consumo):
        self._preco = preco
        self._consumo = consumo

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, valor):
        self._preco = valor

    @property
    def consumo(self):
        return self._consumo

    @consumo.setter
    def consumo(self, valor):
        self._consumo = valor

    def exibe(self):
        print(f"Preço: {self.preco} \nConsumo: {self.consumo}")


class computador(equipamento):
    def __init__(self, preco, consumo, memoria, hd):
        super().__init__(preco, consumo)
        self._memoria = memoria
        self._hd = hd

    @property
    def memoria(self):
        return self._memoria

    @memoria.setter
    def memoria(self, valor):
        self._memoria = valor

    @property
    def hd(self):
        return self._hd

    @hd.setter
    def hd(self, valor):
        self._hd = valor

    def exibe(self):
        super().exibe()
        print(f"Memória: {self._memoria} \nHD: {self._hd}")


class testaequipamento(equipamento):
    def __init__(self, preco1, consumo1, preco2, consumo2, memoria, hd):
        self._preco1 = preco1
        self._preco2 = preco2
        self._consumo1 = consumo1
        self._consumo2 = consumo2
        self._memoria = memoria
        self._hd = hd

    def main(self):
        e = equipamento(self._preco1, self._consumo1)
        c = computador(self._preco2, self._consumo2, self._memoria, self._hd)

        dados = f"""TestaEquipamento
Equipamento:
Preço: {e.preco}
Consumo: {e._consumo}

Computador:
Preço: {c.preco}
Consumo: {c.consumo}
Memória: {c.memoria}
HD: {c.hd}"""
        print(dados)


# Testes
c1 = computador("R$1200", "300W", "8GB", "1TB")
c2 = computador("R$1300", "400W", "12GB", "1TB")
t = testaequipamento("R$1400", "450W", "R$1200", "300W", "8GB", "1TB")
t.main()
