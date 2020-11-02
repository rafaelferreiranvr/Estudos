"""Crie uma classe denominada Elevador para armazenar as informações de
um elevador dentro de um prédio. A classe deve armazenar o andar andarAtual
(térreo = O),
a quantidade de andares no prédio, excluindo o térreo, capacidade do elevador,
e quantas pessoas estão presentes nele.
A classe deve também disponibilizar os seguintes métodos:

Inicializa: que deve receber como parâmetros a capacidade do elevador e o
andares de andares no prédio (os elevadores sempre começam no térreo e vazio)

Entra: para acrescentar uma pessoa no elevador (só deve acrescentar se ainda
houver espaço)

Sai: para remover uma pessoa do elevador (só deve remover se houver alguém
dentro dele)

Sobe: para subir um andar (não deve subir se já estiver no último andar)

Desce: para descer um andar (não deve descer se já estiver no térreo)

Encapsular todos os atributos da classe (criar os métodos set e get).
"""


class elevador:

    def __init__(self, maxpessoas, andares):
        self.maxpessoas = maxpessoas
        self.andares = andares
        self.init2(0, 0)

    def init2(self, andarAtual, p):
        self.andarAtual = andarAtual
        self.p = p

    def entra(self):
        if (self.p + 1) <= self.maxpessoas:
            self.p += 1
        else:
            print("Não cabem mais pessoas nesse elevador.")

    def sai(self):
        if (self.p - 1) != 0:
            self.p -= 1
        else:
            print("Não tem pessoas nesse elevador.")

    def sobe(self):
        if (self.andarAtual + 1) <= self.andares:
            self.andarAtual += 1
        else:
            print("Não é possível subir mais.")

    def desce(self):
        if (self.andarAtual - 1) >= 0:
            self.andarAtual -= 1
        else:
            print("Não é possível descer mais.")


# Testes
e1 = elevador(3, 4)
e1.entra()
e1.entra()
e1.entra()
e1.sai()
e1.sobe()
e1.sobe()
e1.desce()
e1.desce()
e1.desce()
e1.desce()
e1.entra()
e1.entra()
e1.entra()
e1.sai()
e1.sai()
e1.sai()
