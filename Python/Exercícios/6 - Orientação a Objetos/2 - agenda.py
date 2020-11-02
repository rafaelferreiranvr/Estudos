"""Crie uma classe Agenda que pode armazenar 10 pessoas e seja capas de
realizar as seguintes operações:
armazenaPessoa(String nome, int idade, float altura)
removePessoa(String nome)
buscaPessoa(String nome) // informa em que posição da agenda está a pessoa
imprimeAgenda() // imprime os dados de todas as pessoas da agenda
imprimePessoa(int index) // imprime os dados da pessoa que está na
posição "i" da agenda. """


class Agenda:
    global dadosindex
    dadosindex = {}
    global dados
    dados = {}

    def armazenaPessoa(self, nome, idade, altura):
        try:
            str(nome)
            int(idade)
            float(altura)
        except ValueError:
            raise ValueError("Tipos de dados incorretos.")

        valor = f"Nome: {nome} \nIdade: {idade} \nAltura: {altura}\n"
        dadosindex.update({int(f"{len(dadosindex) + 1}"): valor})
        dados.update({nome: f"\nIdade: {idade} \nAltura: {altura}\n"})

    def removePessoa(self, nome):
        try:
            for x in range(1, len(dadosindex) + 1):
                if dadosindex[x] == f"Nome: {nome} {dados[nome]}":
                    break
            dados.pop(nome)
            dadosindex.pop(x)
        except KeyError:
            raise KeyError("Pessoa não encontrada.")

    def buscaPessoa(self, nome):
        try:
            print(f"Nome: {nome} {dados[nome]}")
        except KeyError:
            raise KeyError("Pessoa não encontrada.")

    def imprimeAgenda(self):
        for x in dadosindex:
            print(dadosindex[x])

    def imprimePessoa(self, indice):
        try:
            print(dadosindex[indice])
        except KeyError:
            raise KeyError("Pessoa não encontrada.  ")


# Testes
pessoas = Agenda()
pessoas.armazenaPessoa("Angélica", 12, 1.50)
pessoas.armazenaPessoa("Lucas", 17, 1.82)
pessoas.armazenaPessoa("Márcio", 21, 1.75)
pessoas.armazenaPessoa("Marcos", 14, 1.60)
pessoas.armazenaPessoa("Renato", 19, 1.70)
pessoas.buscaPessoa("Lucas")
pessoas.removePessoa("Lucas")
pessoas.imprimeAgenda()
pessoas.imprimePessoa(4)
