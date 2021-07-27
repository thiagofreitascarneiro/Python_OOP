'''
Crie uma classe Agenda que pode armazenar 10 pessoas e seja capaz de realizar as
seguintes operações:

    * void armazenaPessoa(String nome, int idade, float altura);
    * void removePessoa(String nome);
    * int buscaPessoa(String nome); // informa em que posição da agenda está a pessoa
    * void imprimeAgenda(); // imprime os dados de todas as pessoas da agenda
    * int buscaPessoa(String nome); // imprime os dados da pessoa que está na posição 'i' da agenda.
'''
class Pessoa:

    def __init__(self, nome, idade, altura):
        self.__nome = nome
        self.__idade = idade
        self.__altura = altura


class Agenda:

    agenda = []

    def armazena_pessoa(self, pessoa):
        self.agenda.append(pessoa)


    def imprime_agenda(self):
        print('*** IMPRIMINDO OS DADOS DA AGENDA ***')
        for i in self.agenda:
            print(f'Nome: {i._Pessoa__nome}| Idade: {i._Pessoa__idade} |altura: {i._Pessoa__altura}|')
        print()


    def imprime_pessoa(self, index):
        for p, i in enumerate(self.agenda):
            if p == index:
                print('*** IMPRIMINDO OS DADOS DA PESSOA ***')
                print(f'Dados da pessoa na posição {index}: Nome: {i._Pessoa__nome}| Idade: {i._Pessoa__idade} |altura: {i._Pessoa__altura}|')
        print()


    def busca_pessoa(self, nome):
        for p, i in enumerate(self.agenda):
            if nome == i._Pessoa__nome:
                print('*** INFORMANDO A POSIÇÃO DA AGENDA. ***')
                print(f'A posição da Agenda que a/o {nome} se encontra é na {p} posição.')
            elif nome != i._Pessoa__nome and p == len(self.agenda) - 1:
                print(f'O {nome} não existe na Agenda.')
        print()


    def remover_pessoa(self, nome):
        print('*** REMOVENDO A PESSOA DA AGENDA. ***')
        for i, n in enumerate(self.agenda):
            if nome == n._Pessoa__nome:
                print(f'Removendo o contato {n._Pessoa__nome}')
                del self.agenda[i]
        for i in self.agenda:
            print(f'Nome: {i._Pessoa__nome}| Idade: {i._Pessoa__idade} |altura: {i._Pessoa__altura}|')
        print()



# instancia do objeto para Pessoa
user1 = Pessoa('Bob Jack', 32, 1.85)
user2 = Pessoa('Billy Joe', 39, 1.89)
user3 = Pessoa('Ayn Rand', 69, 1.67)
user4 = Pessoa('Thomas Sowell', 85, 1.99)
user5 = Pessoa('Hermione Granger', 29, 1.65)


# instância do objeto para Agenda
agenda = Agenda()


# Armazenando os dados
Agenda.armazena_pessoa(agenda, user1)
Agenda.armazena_pessoa(agenda, user2)
Agenda.armazena_pessoa(agenda, user3)
Agenda.armazena_pessoa(agenda, user4)
Agenda.armazena_pessoa(agenda, user5)

# testando os comandos
Agenda.imprime_agenda(agenda)

Agenda.remover_pessoa(agenda, 'Bob Jack') #Removendo o contato

Agenda.imprime_pessoa(agenda, 2) #Imprimindo Agenda pela posição.


Agenda.busca_pessoa(agenda, 'Hermione Granger') #nome que existe
Agenda.busca_pessoa(agenda, 'Babu Rangel') #nome não existe na lista















