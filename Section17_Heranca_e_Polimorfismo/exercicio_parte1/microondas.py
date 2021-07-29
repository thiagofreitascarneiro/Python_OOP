'''
Microondas - POO
'''

class Microondas:

    def __init__(self, ligado, porta_microondas):
        self.__ligado = ligado
        self.__porta_microondas = porta_microondas


    def porta_fechada(self, porta):
        if porta == 'S':
            self.__porta_microondas = True
        elif porta == 'N':
            self.__porta_microondas = False


    def ligar_microondas(self, liga_desliga):
        if liga_desliga == 'S':
            if self.__porta_microondas == False:
                self.__ligado = True
                print('Ligando o microondas...')
            else:
                print('A porta do Microondas precisa esta fechada para ligar.')
        elif liga_desliga == 'N':
            self.__ligado = False


    def imprimir(self):
        print(f'Microondas está ligado ? {self.__ligado}')
        print(30 * '=')
        print(f'A porta do microondas está aberta? {self.__porta_microondas}')
        print(30 * '=')


ligar = False
porta = False
micro = Microondas(ligar, porta)


while True:
    abrir_porta = input('Deseja abrir a porta do microondas ? [Sim] ou [Não]: ').upper()[0]
    botao_ligar = input('Deseja ligar o microondas ? [Sim] ou [Não]: ').upper()[0]
    if abrir_porta == 'S':
        Microondas.porta_fechada(micro, abrir_porta)
    elif abrir_porta == 'N':
        Microondas.porta_fechada(micro, abrir_porta)
    if botao_ligar == 'S':
        Microondas.ligar_microondas(micro, botao_ligar)
    elif botao_ligar == 'N':
        Microondas.ligar_microondas(micro, botao_ligar)
    sair = input('Deseja sair: [sim] [não]: ').upper()[0]
    if sair == 'S':
        Microondas.imprimir(micro)
        break



