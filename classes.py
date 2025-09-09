# Criação da Classe LOCADORA, contendo os dicionários e iniciando a classe com seus atributos
class Locadora:
    def __init__(self, nome, cidade, telefone):
        self.__nome = nome
        self.__cidade = cidade
        self.__telefone = telefone

        self.__clientes = {}
        self.__filmes = {}
        self.__jogos = {}



class Item:
    def __init__(self, codigo, titulo, disponivel):
        self.__codigo = codigo # Código único do item
        self.__titulo = titulo # Título do filme/jogo
        self.__disponivel = disponivel # Disponibilidade


        