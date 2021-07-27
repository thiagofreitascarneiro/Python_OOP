'''
Crie uma classe denominada Elevador para armazenar as informações de um elevador
dentro de um prédio. A classe deve armazenar o andar atual (térreo - 0), total de andares
no prédio, ecluibdo o térreo, capacidade do elevador, e quantas pessoas estão presentes
nele.

A classe deve também disponibilizar os seguintes métodos:

    * - Inicializa: que deve receber como parâmetros a capacidade do elevador e o
    total de andares no prédio (os elevadores sempre começam no térreo e vazio);

    * - Entra: para acrescentar uma pessoa no elevador (só deve acrescentar se ainda houver espaço)

    * - Sai: para remover uma pessoa do elevador (só deve remover se houver alguem dentro dele.)

    * - Sobe: para subir um andar (não deve subir se já estiver no último andar);

    * - Desce: para descer um andar (não deve descer se já estiver no térreo);

    * - Encapsular todo os atributos da classe (criar métodos set e get);

'''

class Elevador:

    def __init__(self, andar_atual, total_andares, capacidade_elevador, pessoas_presentes):
        self.__andar_atual = andar_atual
        self.__total_andares = total_andares
        self.__capacidade_elevador = capacidade_elevador
        self.__pessoas_presentes = pessoas_presentes


    def inicializa(self, capacidade_elevador, total_andares):
        print(f'Capacidade do elevador: {capacidade_elevador} pessoas | Total de Andares: {total_andares} ')


    # só deve acrescentar se ainda houver espaço.
    def entra(self, pessoa, pessoas_presentes, capacidade_elevador):
        disponivel = capacidade_elevador - pessoas_presentes
        if self.__pessoas_presentes == 6:
            pass
        else:
            if pessoas_presentes < capacidade_elevador:
                print(f'Ainda pode entrar o total de |{disponivel}| pessoas.')
            if pessoa > disponivel:
                print(f'O elevador não suporta mais que {self.__capacidade_elevador} pessoas.')
                while pessoa > disponivel:
                    pessoa = int(input('digite a quantidade de pessoas permitida: '))
            if pessoa <= disponivel:
                print(f'quantidade de |{pessoa}| pessoas adicionada com sucesso.')
                self.__pessoas_presentes = pessoas_presentes + pessoa


    # só deve remover se houver alguém dentro dele.
    def sai(self, pessoa):
        retirada = self.__pessoas_presentes - pessoa
        if self.__capacidade_elevador == 0:
            print('O elevador está vazio.')
        else:
            if retirada < 0:
                print(f'Não há como remover {pessoa} pessoas do elevador, o elevador só possui {self.__pessoas_presentes} pessoas.')
                while retirada < 0:
                    pessoa = int(input('Digite a quantidade de pessoas que deseja retirar que estão presentes no elevador: '))
                    retirada = self.__pessoas_presentes - pessoa
                    if retirada >= 0:
                        print(f'Removendo o total de {pessoa} pessoas do elevador.')
            else:
                print(f'Removendo o total de {pessoa} pessoas do elevador.')



    # não deve subir se já estiver no último andar.
    def sobe(self, total_andares, andar_atual, sobe_andar):
        andar = andar_atual + sobe_andar
        if andar > total_andares:
            print(f'não há como subir, estamos no {andar_atual}º andar, só vamos até o {total_andares}º andar.')
            while andar > total_andares:
                sobe_andar = int(input('Deseja subir quantos andares: '))
                andar = andar_atual + sobe_andar
                self.__andar_atual = andar
        if andar <= total_andares:
            print(f'Subindo para o |{andar}º| andar')
            self.__andar_atual = andar


    # Não deve descer se já estiver no térreo.
    def desce(self, desce_andar):
        descer = self.__andar_atual - desce_andar
        if descer <= 0:
            print(f'Não há como descer, estamos no |{self.__andar_atual}º| andar.')
            while descer < 0:
                desce_andar = int(input('Deseja descer quantos andares: '))
                descer = self.__andar_atual - desce_andar
        else:
            desce_andar = descer
            print(f'Descendo para o |{desce_andar}º| andar')



# Instância do objeto
total = 10
andar = int(input('Obs: O elevador só possui 10 andares. Digite o andar atual:  '))
if andar > total:
    andar = int(input('Obs: O elevador só possui 10 andares. Digite o andar atual:  '))

capacidade = 6
pessoas = int(input('Quantidade de pessoas presentes no elevador: '))
if pessoas > capacidade:
    pessoas = int(input('ELEVADOR NÃO SUPORTA! digite até 6 pessoas: '))


#Objeto
predio = Elevador(andar, total, capacidade, pessoas)

Elevador.inicializa(predio, capacidade, total)

entrar_pessoa = int(input('Digite o total de pessoas para entrar no elevador: '))
Elevador.entra(predio, entrar_pessoa, pessoas, capacidade)

remover_pessoa = int(input('Quantas pessoas deseja remover: '))
Elevador.sai(predio, remover_pessoa)

andar_desejado = int(input('quanto andares deseja subir: '))
Elevador.sobe(predio, total, andar, andar_desejado)

andar_desejado_descer = int(input('quanto andares deseja descer: '))
Elevador.desce(predio, andar_desejado_descer)




