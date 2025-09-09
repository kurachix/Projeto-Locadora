# Criação da Classe LOCADORA, contendo os dicionários e iniciando a classe com seus atributos
class Locadora:
    def __init__(self, nome, cidade, telefone):
        self.__nome = nome
        self.__cidade = cidade
        self.__telefone = telefone

        self.__clientes = {}
        self.__filmes = {}
        self.__jogos = {}
        


    # Funções Relacionadas as ações dos usuarios na locadora
    def cadastroJogo(self, codigo, titulo, disponivel): # Adiciona item à lista
        self.__jogos[len(self.__jogos) + 1] = Jogos(codigo=codigo, titulo=titulo, disponivel=disponivel)

    def cadastroFilme(self, codigo, titulo, disponivel): # Adiciona item à lista
        self.__filmes[len(self.__filmes) + 1] = Filmes(codigo=codigo, titulo=titulo, disponivel=disponivel)

    def cadastrasCliente(self, nome, cpf, itensLocados): # Adiciona cliente à lista
        self.__clientes[len(self.__clientes) + 1] = Clientes(nome=nome, cpf=cpf, itensLocados=itensLocados)

    def listarClientes(): # Mostra todos os clientes cadastrados
        pass

    def listarItens(self): # Mostra todos os itens cadastrados
        return self.__jogos, self.__filmes
    
    def listarFilmes(self):
        return self.__filmes
    
    def listarJogos(self):
        return self.__filmes
    



class Item:
    def __init__(self, codigo, titulo, disponivel):
        self.__codigo = codigo # Código único do item
        self.__titulo = titulo # Título do filme/jogo
        self.__disponivel = disponivel # Disponibilidade

    # ----------------- -------------------------
    #Metodos GETs

    def getTitulo(self):
        return self.__titulo
    
    def getCodigo(self):
        return self.__codigo
    
    def getDisponivel(self):
        return self.__disponivel
    
    # ----------------- -------------------------
    #Metodos SETs

    def setTitulo(self, titulo):
        self.__titulo = titulo
        return self.__titulo
    
    def setCodigo(self, codigo):
        self.__codigo = codigo
        return self.__codigo
    
    def setDisponivel(self, disponivel):
        self.__disponivel = disponivel
        return self.__disponivel
    
    # ----------------- -------------------------
    #Metodos Funções

    def alugarFilmes():
        pass

    def alugarJogos():
        pass

    def devolverJogos():
        pass

    def devolverFilmes():
        pass
    


class Jogos(Item):
    def __init__(self, codigo, titulo, plataforma, faixaEtaria):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__plataforma = plataforma
        self.__faixaEtaria = faixaEtaria
        

        

class Filmes(Item):
    def __init__(self, codigo, titulo, genero, duracao):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__genero = genero
        self.__duracao = duracao




class Clientes():
    def __init__(self, nome, cpf, itensLocados):
        self.__nome = nome
        self.__cpf = cpf
        self.__itensLocados = itensLocados

    
    def locar(): # Cliente aluga um item
        pass

    def devolver(): # Cliente devolve um item
        pass

    def listarItens(): # Mostra todos os itens alugados
        pass


    
        
    





        