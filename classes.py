# Criação da Classe LOCADORA, contendo os dicionários e iniciando a classe com seus atributos
class Locadora:
    def __init__(self, nome, cidade, telefone):
        self.__nome = nome
        self.__cidade = cidade
        self.__telefone = telefone

        self.__clientes = []
        self.__itens = []  # única lista
        self.__itensLocados = []


    def cadastroJogo(self, titulo, plataforma, faixaEtaria):
        self.__itens.append(Jogos(titulo, plataforma, faixaEtaria, True))

    def cadastroFilme(self, titulo, genero, duracao):
        self.__itens.append(Filmes(titulo, genero, duracao, True))

    def cadastroCliente(self, nome, cpf, itensLocados):
        self.__clientes.append(Clientes(nome, cpf, itensLocados))

    def listarClientes(self):
        return self.__clientes

    def listarItens(self):
        return self.__itens


    



class Item:
    def __init__(self, titulo, disponivel):
        self.__titulo = titulo # Título do filme/jogo
        self.__disponivel = disponivel # Disponibilidade

    # ----------------- -------------------------
    #Metodos GETs

    def getTitulo(self):
        return self.__titulo
    
    def getDisponivel(self):
        return self.__disponivel
    
    # ----------------- -------------------------
    #Metodos SETs

    def setTitulo(self, titulo):
        self.__titulo = titulo
        return self.__titulo
    
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
    def __init__(self, titulo, plataforma, faixaEtaria, disponivel=True):
        super().__init__(titulo, disponivel)
        self.__plataforma = plataforma
        self.__faixaEtaria = faixaEtaria

    def __str__(self):
        return f"Jogo: {self.getTitulo()} | Plataforma: {self.__plataforma} | Faixa Etária: {self.__faixaEtaria}"
    
        

        

class Filmes(Item):
    def __init__(self, titulo, genero, duracao, disponivel=True):
        super().__init__(titulo, disponivel)
        self.__genero = genero
        self.__duracao = duracao

    def __str__(self):
        return f"Filme: {self.getTitulo()} | Gênero: {self.__genero} | Duração: {self.__duracao} min"





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


    
        
    





        