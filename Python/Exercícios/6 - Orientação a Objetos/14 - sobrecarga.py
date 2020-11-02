"""Crie um novo pacote chamado sobrecarga. Crie uma classe Pessoa.
Na classe Pessoa crie 3 variáveis de instância: código, nome e idade. Crie um
método exibe(), que exiba o conteúdo de todas as variáveis declaradas na
classe em questão.
Crie uma sobrecarga do método exibe() que receba como parâmetro um número
inteiro e decida por meio do valor desse parâmetro se a idade será exibida ou
não. Para isso use o seguinte critério: se o valor do parâmetro for igual a 1,
imprima idade, se não, não imprima a idade, mas apenas as outras variáveis de
instância.
Crie um construtor padrão explícito para a classe Pessoa, esse construtor
deverá exibir uma mensagem: "Construtor padrão"
Crie uma classe chamada TestaPessoa que instancie um objeto da classe Pessoa
usando o construtor padrão.
Ainda na classe TestaPessoa, inicialize as variáveis de instância: código,
nome e idade com valores à sua escolha e acione o método exibe(), sem nenhum
parâmetro.
Repita a operação anterior, acionando o método exibe(), passando a
ele um argumento inteiro de valor 1 Repita o que foi feito anteriormente,
só que desta vez, passando um argumento diferente de 1.
Crie um construtor sobrecarregado que permita instanciar objetos com os 3
valores sendo inicializados por valores passados como parâmetros.
Na classe TestaPessoa instancie um objeto usando o segundo construtor (com os
3 parâmetros).
Exiba os dados do objeto que foi instanciado anteriormente por meio do
método exibe() sem argumentos.
"""


class pessoa:
    def __init__(self, codigo, nome, idade):
        self._codigo = codigo
        self._nome = nome
        self._idade = idade
        print("Construtor padrão.")

    def exibe(self, valor=0):
        if valor == 1:
            dado = f"""Código: {self._codigo}
Nome: {self._nome}
Idade: {self._idade}"""
            print(dado)
        else: 
            dado = f"""Código: {self._codigo}
Nome: {self._nome}"""
            print(dado)


class testaPessoa(pessoa):
    def __init__(self, codigo, nome, idade):
        self._codigo = codigo
        self._nome = nome
        self._idade = idade
        p = pessoa(self._codigo, self._nome, self._idade)
        p.exibe()
        p.exibe(1)
        p.exibe(3)
        print("Segundo construtor.")


# Testes
p = pessoa(123454, "Joana", 16)
p.exibe()
tp = testaPessoa(127454, "Jonas", 17)
tp.exibe()