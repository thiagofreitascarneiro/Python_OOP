'''
1 - Crie um novo pacote com o nome: heranca. Todas as (três) classes criadas abaixo deverão ser
salvas neste pacote.

2- Crie uma classe equipamento com dois atributos privados.

3 - Crie uma classe Computador com dois atributos á sua escolha, também privados. A classe Computador
deverá herdar tudo da classe equipamento.

4 - Crie os métodos de acesso e de modificação para todos os atributos definidos em ambas as classes.

5 - Crie uma classe TestaEquipamento, que deverá conter o método main(), crie nela um objeto da classe
equipamento e instancie os dois atributos que você declarou na classe Equipamento. Crie também um objeto
da classe Computador, utilizando os dois atributos declarados na própria classe e os dois herdados da
classe Equipamento.

6 - O método main() deve exibir as informações dos dois objetos criados.

7 - Criar o método exibe() na classe Equipamento parar mostrar os dados dessa classe.

8 - Criar o método exibe() na classe Computador, aproveitando o que já está escrito na superclasse
Equipamento.
'''

class Equipamento:

    def __init__(self, mouse, teclado):
        self.__mouse = mouse
        self.__teclado = teclado


    def mostra_equipamentos(self):
        print(f'Equipamento 1: {self.__mouse}. Equipamento 2: {self.__teclado}')


class Computador(Equipamento):

    def __init__(self, cabo, notebook, mouse, teclado):
        super().__init__(mouse, teclado)
        self.__cabo = cabo
        self.__notebook = notebook

    # Reescrevendo o método mostra_equipamentos da classe equipamento
    def mostra_equipamentos(self):
        print(f'Equipamento 1: {self.__notebook}. Equipamento 2: {self._Equipamento__teclado}. Equipamento 3: {self._Equipamento__mouse}. Equipamento 4: {self.__cabo}. ')


class TestaEquipamento:

    def __init__(self):
        self.__equip = Equipamento('Mouse Desktop 850', 'Teclado Desktop 850')
        self.__pc = Computador('HDMI', 'DELL - Notebook Inspiron 15', 'Mouse Desktop 850', 'Teclado Desktop 850')


    def main(self):
        Equipamento.mostra_equipamentos(self.__equip)
        Computador.mostra_equipamentos(self.__pc)


teste = TestaEquipamento()
TestaEquipamento.main(teste)

