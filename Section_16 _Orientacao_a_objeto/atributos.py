'''

Detalhado - https://diegomariano.com/principios-da-orientacao-a-objetos/

POO - Atributos

Atributos - Representam as características do objeto. Ou seja, pelos atributos
nós conseguimos representar computacionalmente os estados de um objetos.


Em python, dividimos os atributos em 3 grupos:
    - Atributos de Instância;
    - Atributos de Classe;
    - Atributos Dinâmico;


# Atributos de instância: São atributos delcarados dentro do método construtor.

# OBS: Método construtor: É um método especial utilizado para a construção do objeto.

# Em Python, por convenção, ficou estabelecido que, todo atributo de uma classe é público.
Ou seja, pode ser acessado em todo o projeto.
Caso queiramos demonstrar que determinado atributo deve ser tratado como privado, ou seja,
que deve ser acessado/utilizado somente dentro da própria classe onde está declarado,
utiliza - se __ duplo underscore no início de seu nome.

Isso é conhecido também como Name Mangling.


# OBS: Lembre-se que isso é apenas uma convenção, ou seja, a linguagem Python não
# vai impedir que façamos acesso aos atributos sinalizados como privados fora da classe.



# O que significa atributos de instância?

# Siginifica, que ao criarmos instâncias/objetos de uma classe, todas as instâncias
# terão estes atributos.

user1 = Acesso('user1@gmail.com', '123456')
user2 = Acesso('user2@gmail.com', '123435')

print(40 * '=')
print(' ')
user1.mostra_email()
user2.mostra_email()

# Atributos de Classe


'''

# Classes com Atributo de Instancia Publico.
class Lampada:

    def __init__(self, voltagem, cor):
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False


class ContaCorrente:

    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo


class Produto:

    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor


class Usuario:

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha


# Atributos Públicos e Atributos Privados

class Acesso:

    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha

    def mostra_senha(self):
        print(self.__senha)

    def mostra_email(self):
        print(self.email)

p1 = Produto('Playstation 4', 'Video game,', 2300)
p2 = Produto('Xbox S', 'Video game,', 4500)



# Atributos de classe, são atributos, claro, que são declarados diretamente na classe, ou seja,
# fora do construtor. Geralmente já inicializamos um valor, e este é compartilhado entre
# todas as instâncias da classe. Ou seja, ao invés de cada instância de classe ter seus prórios
# valores como é o caso dos atributos de instância, com os atributos de classe todas as intâncias
# terão o mesmo valor para este atributo.

# Refatorar a classe Produto

class Produto:

    # Atributo de classe
    imposto = 1.05  # 0.05% de imposto
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        Produto.contador = self.id # contador é um atributo da classe


p1 = Produto('Playstation 4', 'Video game', 2300)
p2 = Produto('Xbox S', 'Video game', 4500)

print(p1.valor)  # Acesso possível, mas incorreto de um atributo de classe
print(p2.valor)  # Acesso possível, mas incorreto de um atributo de classe

# OBS: Não precisamos criar uma instância de uma classe para fazer acesso a um atributo de classe

print(Produto.imposto) # Acesso correto de um atributo de classe

print(p1.id)
print(p2.id)

# OBS: Em linguagens como o Java, os atributos conhecidos como atributos de classe aqui em Python
# são chamados de atributos estáticos;



# Atributos Dinâmicos - Um atributo de instância que pode ser criado em tempo de execução.

# OBS: O atributo dinâmico será exclusivo da instância que o criou.

p1 = Produto('Playstation 4', 'Video Game', 2300)

p2 = Produto('Arroz', "Mercearia", 5.99)

# Criando um atributo dinâmico em tempo de execução
# ele é exclusivo da instância que o criou.

p2.peso = '5kg'   # Note que na classe Produto não existe o atributo peso

print(f'Produto: {p2.nome}, Descrição: {p2.descricao}, Valor: {p2.valor}, Peso: {p2.peso}')

#print(f'Produto: {p1.nome}, Descrição: {p1.descricao}, Valor: {p1.valor}, Peso: {p1.peso}')

# Deletando atributos

print(p1.__dict__)
print(p2.__dict__)

#print(Produto.__dict__)

del p2.peso
del p2.valor
del p2.descricao

print(p1.__dict__)
print(p2.__dict__)

