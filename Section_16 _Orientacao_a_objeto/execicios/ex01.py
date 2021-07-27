'''
Crie uma classe para representar uma pessoa, com os atributos privados de nome, idade
e altura. Crie os métodos públicos necessários para sets e gets e também um método
para imprimir os dados de uma pessoa.
'''

class Pessoa:

    def __init__(self, nome, idade, altura):
        self.__nome = nome
        self.__idade = idade
        self.__altura = altura


    def mostra_nome(self):
        return self.__nome


    def mostra_idade(self):
        return self.__idade


    def mostra_altura(self):
        return self.__altura


user = Pessoa('Bob Jack', 32, 1.85)
print(Pessoa.mostra_nome(user))
print(Pessoa.mostra_idade(user))
print(Pessoa.mostra_altura(user))
