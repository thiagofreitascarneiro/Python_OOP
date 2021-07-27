'''
Crie uma classe Televisão e uma classe ControleRemoto que pode controlar o volume
e trocar os canais de televisão.

    * - O controle de volume permite aumentar ou diminuir a potência do volume
    de som em uma unidade de cada vez;

    * - O controle de canal também permite aumentar e diminuir o número do canal
    em uma unidade, porém, também possibilita trocar para um canal indicado;

    * - Também devem existir métodos para consultar o valor do volume de som e o canal
    selecionado.
'''

class Televisao():

    def __init__(self, volume=1, canais=1):
        self.__volume = volume
        self.__canais = canais


class ControleRemoto(Televisao):

    def __init__(self, volume, canais):
        super().__init__(volume, canais)
        self.__volume = volume
        self.__canais = canais


    def controle_volume(self, alterando_volume):
        if alterando_volume == '+':
            if self.__volume < 100:
                self.__volume = self.__volume + 1
            else:
                print('A TV já está no volume maximo.')
        elif alterando_volume == '-':
            if self.__volume > 1:
                self.__volume = self.__volume - 1
            else:
                print('A TV já está no menor volume.')


    def controle_canal(self, alterando_canais):
        if alterando_canais == '+':
            if self.__canais < 30:
                self.__canais = self.__canais + 1
            else:
                print('A TV só possui 30 canais.')
        elif alterando_canais == '-':
            if self.__canais > 1:
                self.__canais = self.__canais - 1
            else:
                print('Canal já está no minimo')

    def consulta_som(self, mostra_som):
        if mostra_som == 'S':
            print(f'Volume: {self.__volume}')

    def consulta_canal(self, mostra_canal):
        if mostra_canal == 'S':
            print(f'Canal: {self.__canais}')


#Instância do objeto.

tv = Televisao()

controle = ControleRemoto(1, 1)

# Controle do volume
while True:
    volume = str(input('Controle de volume: [+] [-] ou x para parar: '))
    ControleRemoto.controle_volume(controle, volume)
    if volume == 'x':
        break
print(40 * '=')
# Controle dos canais
while True:
    canal = str(input('Controle do canal: [+] [-] ou x para parar: '))
    ControleRemoto.controle_canal(controle, canal)
    if canal == 'x':
        break


volume = str(input('Deseja consultar o volume: [S] ou [N]: ')).upper()[0]
ControleRemoto.consulta_som(controle, volume)
print(40 * '=')
canal = str(input('Deseja consultar o canal: [S] ou [N]: ')).upper()[0]
ControleRemoto.consulta_canal(controle, canal)







