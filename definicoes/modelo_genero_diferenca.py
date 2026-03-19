# Exemplo de definição por gênero e diferença
#
# Autor: Fabrício Galende Marques de Carvalho

from datetime import date

class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def dizer_nome(self):
        print("Meu nome é ", self.nome)

class Aluno(Pessoa):
    def __init__(self, nome, curso):
        super().__init__(nome)
        self.curso = curso

    def apresentar_se(self):
        self.dizer_nome()
        print("Sou aluno(a) do curso de ", self.curso)

