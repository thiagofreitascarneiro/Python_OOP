'''
POO - Herança (Inheritance)

A ideia de herança é a reaproveitar código. Também extender classes.

OBS: Com a herança, a partir de uma classe existente, nós extendemos outra classe
que passa a herdar atributos e métodos da classe herdada.


Cliente
    - nome;
    - sobrenome;
    - cpf;
    - renda;

Funcionario
    - nome;
    - sobrenome;
    - cpf;
    - matricula;

Pergunta: Existe alguma entidade genérica o suficiente para encapsular os atributos
e métodos comuns  a outras entidades ?


class Cliente:

    def __init__(self, nome, sobrenome, cpf, renda):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.cpf = cpf
        self.__renda = renda

    def nome_completo(self):
        return f'{self.__nome}  {self.__sobrenome}'


class Funcionario:

    def __init__(self, nome, sobrenome, cpf, matricula):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__matricula = matricula

    def nome_completo(self):
        return f'{self.__nome}  {self.__sobrenome}'


cliente1 = Cliente('Agenlina', 'Jolie', '123.456.789-00', 5000)
funcionario1 = Funcionario('Felicity', 'Jone', '987.654.321-11', 1234)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())

OBS: Quando uma classe herda de outra classe ela herda TODOS os atributos e métodos da classe herdada.

Quando uma classe herda de outra classe, a classe herdada é conhecida por:
    - Super Classe;
    - Classe Mãe;
    - Classe Pai;
    - Classe base;
    - Classe Genérica;

Quando uma classe herda de outra classe, ela é chamada:
    [Cliente, Funcionario]
    - Sub Classe;
    - Classe Filha;
    - Classe Específica;

class Pessoa:

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome}  {self.__sobrenome}'


class Cliente(Pessoa):
    #Cliente herda de Pessoa

    def __init__(self, nome, sobrenome, cpf, renda):
        super().__init__(nome, sobrenome, cpf) # Forma de acessar dados da superclasse
        self.__renda = renda


class Funcionario(Pessoa):
    #funcionario herda de Pessoa

    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula


cliente1 = Cliente('Agenlina', 'Jolie', '123.456.789-00', 5000)
funcionario1 = Funcionario('Felicity', 'Jone', '987.654.321-11', 1234)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())

print(cliente1.__dict__)

print(funcionario1.__dict__)

#Sobrescrita de Métodos (Overriding)
Sobrescrita de método, ocorre quando reescrevemos/reimplementamos um método presente na super classe
em classes filhas.
'''
class Pessoa:

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome}  {self.__sobrenome}'


class Cliente(Pessoa):
    #Cliente herda de Pessoa

    def __init__(self, nome, sobrenome, cpf, renda):
        super().__init__(nome, sobrenome, cpf) # Forma de acessar dados da superclasse
        self.__renda = renda


class Funcionario(Pessoa):
    #funcionario herda de Pessoa

    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula

    def nome_completo(self):
        print(super().nome_completo())
        print(self._Pessoa__cpf)
        return f'Funcionario: {self.__matricula}  Nome: {self._Pessoa__nome}'

# Sobrescrita de Métodos (Overriding)

cliente1 = Cliente('Agenlina', 'Jolie', '123.456.789-00', 5000)
funcionario1 = Funcionario('Felicity', 'Jone', '987.654.321-11', 1234)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())




