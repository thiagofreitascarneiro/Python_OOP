'''

03 - Escreva um código que apresente a classe Quadrado, com atributos lado, área e perimetro e,
os métodos calcularArea, calcularPerimetro e imprimir. Os métodos calcularArea e calcularPerimetro
devem efetuar seus respectivos cálculos e colocar os valores nos atributos area e perimetro. O método
imprimir deve mostrar na tela os valores de todos os atributos. Salienta-se que área de um quadrado é
obtida plea fórmula (lado * lado) e o perímetro por (4 * lado).

04 - Baseando-se no exercício 3 adicione um método construtor que permita a definição de todos
os atributos no momento da instanciação do objeto.

'''

class Quadrado:

    def __init__(self, lado):
        self.__lado = lado
        self.__area = 0
        self.__perimetro = 0


    def calcula_area(self):
        self.__area = lado * lado


    def calcula_perimetro(self):
        self.__perimetro = lado * 4


    @property
    def imprimir(self):
        return f'Area do Quadrado: {self.__area}, Area do Perímetro: {self.__perimetro}'


# instancia do objeto
lado = 2
quadrado = Quadrado(lado)

Quadrado.calcula_perimetro(quadrado)
Quadrado.calcula_area(quadrado)

# usando property o acesso é sem os parenteses (Getter)
resultado_quadrado = quadrado.imprimir
print(resultado_quadrado)


