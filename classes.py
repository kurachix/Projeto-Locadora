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
    def cadastroJogo(self, codigo, titulo, plataforma, faixaEtaria): # Adiciona item à lista
        self.__jogos[len(self.__jogos) + 1] = Jogos(codigo=codigo, titulo=titulo, plataforma=plataforma, faixaEtaria=faixaEtaria)

    def cadastroFilme(self, codigo, titulo, genero, duracao): # Adiciona item à lista
        self.__filmes[len(self.__filmes) + 1] = Filmes(codigo=codigo, titulo=titulo, genero=genero, duracao=duracao)

    def cadastrasCliente(self, nome, cpf, itensLocados): # Adiciona cliente à lista
        self.__clientes[len(self.__clientes) + 1] = Clientes(nome=nome, cpf=cpf, itensLocados=itensLocados)

    def listarClientes(self): # Mostra todos os clientes cadastrados
        pass

    def listarItens(self): # Mostra todos os itens cadastrados
        return self.__jogos, self.__filmes
    
    def listarFilmes(self):
        return self.__filmes
    
    def listarJogos(self):
        return self.__jogos
    



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

    def alugarFilmes(self):
        pass

    def alugarJogos(self):
        pass

    def devolverJogos(self):
        pass

    def devolverFilmes(self):
        pass
    


class Jogos(Item):
    def __init__(self, codigo, titulo, plataforma, faixaEtaria, disponivel=True):
        super().__init__(codigo, titulo, disponivel)
        self.__plataforma = plataforma
        self.__faixaEtaria = faixaEtaria
        

        

class Filmes(Item):
    def __init__(self, codigo, titulo, genero, duracao, disponivel=True):
        super().__init__(codigo, titulo, disponivel)
        self.__genero = genero
        self.__duracao = duracao




class Clientes():
    def __init__(self, nome, cpf, itensLocados):
        self.__nome = nome
        self.__cpf = cpf
        self.__itensLocados = itensLocados

    
    def locar(self): # Cliente aluga um item
        pass

    def devolver(self): # Cliente devolve um item
        pass

    def listarItens(self): # Mostra todos os itens alugados
        pass


    
        
    





        