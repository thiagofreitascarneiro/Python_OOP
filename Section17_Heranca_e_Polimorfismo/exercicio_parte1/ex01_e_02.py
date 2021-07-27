'''
1 - Escreva um código que apresente a classe Pessoa, com atributos nome, endereço,
telefone e, o método imprimir. O método imprimir deve mostrar na tela os valores
de todos os atributos.

2 - Baseando-se no exercicio 1 adicione um método que permita a definição de todos os atributos no
momento da instanciação do objeto.
'''

class Pessoa:

    def __init__(self, nome, endereco, telefone):
        self.__nome = nome
        self.__endereco = endereco
        self.__telefone = telefone

    def imprimir(self):
        return f'Nome: {self.__nome} Endereço: {self.__endereco}, Contato: {self.__telefone}'

nome = 'Bob'
endereco = 'Rua Bauru nº 91'
telefone = '11 95588-7799'

pessoa = Pessoa(nome, endereco, telefone)
print(Pessoa.imprimir(pessoa))
