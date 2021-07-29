class Pessoa:

    def __init__(self, codigo=12345, nome='Bob Jack', idade='29'):
        print('Construtor Padrão!')
        self.__codigo = codigo
        self.__nome = nome
        self.__idade = idade


    def exibe(self, imprimir):
        if imprimir == 1:
            print(f'idade: {self.__idade}')
        else:
            print(f'codigo: {self.__codigo} nome: {self.__nome}')



class TestaPessoa:

    def __init__(self):
        self.__cadastro = Pessoa()

        Pessoa.exibe(self.__cadastro, 1)

        Pessoa.exibe(self.__cadastro, 2)



TestaPessoa()
