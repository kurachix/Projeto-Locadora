# Criação da Classe LOCADORA, contendo os dicionários e iniciando a classe com seus atributos
class Locadora:
    def __init__(self, nome, cidade, telefone):
        self.__nome = nome
        self.__cidade = cidade
        self.__telefone = telefone

         # Lista pra armazenarcos clientes e itens 
        self.__clientes = [] # lista pra cadastrar os clientes
        self.__itens = []  # lista de itens (clientes e jogos)

    # -----------------------------
    # Métodos de cadastro
    # -----------------------------

    def cadastroJogo(self, titulo, plataforma, faixaEtaria):
        self.__itens.append(Jogos(titulo, plataforma, faixaEtaria, True))

    def cadastroFilme(self, titulo, genero, duracao):
        self.__itens.append(Filmes(titulo, genero, duracao, True))

    def cadastroCliente(self, nome, cpf, itensLocados):
        self.__clientes.append(Clientes(nome, cpf, itensLocados))


    # -----------------------------
    # Métodos de listagem
    # -----------------------------


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
    


class Jogos(Item):
    def __init__(self, titulo, plataforma, faixaEtaria, disponivel=True):
        super().__init__(titulo, disponivel) # chama o construtor da classe item, herdando memo
        self.__plataforma = plataforma # plataforma do jogo 
        self.__faixaEtaria = faixaEtaria # requisita a faixa etaria do jogo

    def __str__(self):
        # representa o objeto como string, pra nao exibir um monte de codigo 
        return f"Jogo: {self.getTitulo()} | Plataforma: {self.__plataforma} | Faixa Etária: {self.__faixaEtaria}"
    
        


class Filmes(Item):
    def __init__(self, titulo, genero, duracao, disponivel=True):
        super().__init__(titulo, disponivel) # chama o construtor da classe item, herdando memo
        self.__genero = genero # genero do filme
        self.__duracao = duracao # duracao do filme

    def __str__(self):
        # representa o objeto como string, pra nao exibir um monte de codigo
        return f"Filme: {self.getTitulo()} | Gênero: {self.__genero} | Duração: {self.__duracao} min"


class Clientes():
    def __init__(self, nome, cpf, itensLocados):
        self.__nome = nome # nome do cliente
        self.__cpf = cpf #cpf do cliente
        self.__itensLocados = itensLocados #mostra os itens q foram emprestados



    
        
    





        