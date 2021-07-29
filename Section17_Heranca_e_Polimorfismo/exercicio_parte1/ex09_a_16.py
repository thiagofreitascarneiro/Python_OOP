'''
09 ao 16 - Escreva um código que apresente a classe Moto, com atributos marca,
modelo, cor e marcha e, o método imprimir. O método imprimir deve mostrar
na tela os valores de todos os atributos. O atributo marcha indica em que
marcha a Moto se encontra no momento, sendo representado de forma inteira, onde
0 - neutro, 1 - primeira, 2 - segunda, etc..

- adicionar marcha

- adicionar ligar moto
'''

class Moto:

    def __init__(self, marca, modelo, cor, marcha, ligar):
        self.__marca = marca
        self.__modelo = modelo
        self.__cor = cor
        self.__marcha = marcha
        self.__ligar = ligar


    def marcha_acima(self, subir):
        self.__marcha = subir
        if self.__marcha >= 1 and self.__marcha <= 5:
            pass
        else:
            print('A marcha está no limite.')


    def marcha_abaixo(self, descer):
        self.__marcha = descer
        if self.__marcha <= 5 and self.__marcha > 0:
            pass
        else:
            print('A marcha está no limite.')


    def ligada(self, liga_desliga):
        if liga_desliga is True:
            self.__ligar = True
        elif liga_desliga is False:
            self.__ligar = False


    def imprimir(self):
        marchas = {'neutro': 0, 'primeira': 1, 'segunda': 2, 'terceira': 3, 'quarta': 4, 'quinta': 5}
        print(f'A marca: {self.__marca}')
        print(f'Modelo: {self.__modelo}')
        print(f'Cor: {self.__cor}')
        print(f'A moto está ligada ? {self.__ligar}')
        for k, v in marchas.items():
            if self.__marcha == v:
                print(f'Se encontra na Marcha: {k} : {v}')


marcha = 0
contador = 0
ligar = False
while True:
    print(30 * '==')
    moto = Moto('Yamaha', 'NMAX 160 ABS STAR WARS', 'Azul', marcha, ligar)
    if contador == 0:
        ligar_moto = input('Deseja ligar a moto ? [S] sim ou [N] não: ').upper()[0]
        while ligar_moto != 'N' and ligar_moto != 'S':
            print('Digite SIM ou NÃO')
            ligar_moto = input('Deseja ligar a moto ? [S] sim ou [N] não: ').upper()[0]
        if ligar_moto == 'S':
            ligar = True
            Moto.ligada(moto, ligar)
        elif ligar_moto == 'N':
            ligar = False
            Moto.ligada(moto, ligar)
    valor = input('Deseja aumentar a marcha ? [+]: aumenta ou [-]: reduz =  ')
    if valor == '+':
        marcha = marcha + 1
        Moto.marcha_acima(moto, marcha)
        moto = Moto('Yamaha', 'NMAX 160 ABS STAR WARS', 'Azul', marcha, ligar)
        Moto.imprimir(moto)
    elif valor == '-':
        marcha = marcha - 1
        Moto.marcha_abaixo(moto, marcha)
        moto = Moto('Yamaha', 'NMAX 160 ABS STAR WARS', 'Azul', marcha, ligar)
        Moto.imprimir(moto)
    parar = input('Deseja continuar: Sim ou Não: ').upper()[0]
    while parar != 'N' and parar != 'S':
        print('Digite SIM ou NÃO')
        parar = input('Deseja continuar: Sim ou NÃO: ').upper()[0]
    if parar == 'N':
        break
    contador = contador + 1



