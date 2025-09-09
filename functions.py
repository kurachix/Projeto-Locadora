# Importando do classes.py
from classes import *

# Importando as bibliotecas que vao ser utilizadas
import os
import time

LocadoraDoCarlao = Locadora("Locadora_do_Carlão", "Jundiai-SP", "11 961863232")

def cadastro_itens():

    while True:
        os.system("cls")

        print(30 * "-")
        print("CADASTRO DE ITENS".center(30))
        print(30 * "-")

        print("\nO que deseja cadastrar hoje?")
        print("\n1 -> Jogo")
        print("2 -> Filme")
        print("0 -> Voltar")

        cadastro_escolha = int(input("\n Qual a sua escolha? ->"))


        if cadastro_escolha == 1:
            
            os.system("cls")

            titulo = input("Qual o titulo do jogo?\n-->")

            os.system("cls")
            
            plataforma = input("Qual a plataforma do jogo?\n-->")

            os.system("cls")

            faixaEtaria = input("Qual a faixa etaria do jogo?\n-->")
            
            
            LocadoraDoCarlao.cadastroJogo(titulo=titulo, plataforma=plataforma, faixaEtaria=faixaEtaria)
            
            os.system("cls")
            print("Jogo adicionado com sucesso, verifique na lista de jogos")
            
            while True:
                continuar = int(input("1 - Adicionar outro produto\n0 - Sair\n--> "))
                
                if continuar == 1 or continuar == 0:
                    break
            
            if continuar == 0:
                break

        if cadastro_escolha == 2:

            os.system("cls")

            titulo = input("Qual o titulo do filme?\n-->")

            os.system("cls")

            genero = input("Qual o genero do filme?\n-->")

            os.system("cls")

            duracao = input("Qual a duração do filme\n-->")

            LocadoraDoCarlao.cadastroFilme(titulo=titulo, genero=genero, duracao=duracao)

            while True:
                continuar = int(input("1 - Adicionar outro produto\n0 - Sair\n--> "))
                
                if continuar == 1 or continuar == 0:
                    break
            
            if continuar == 0:
                break

def listar_itens():
    os.system("cls")

    print(50 * "-")
    print("Listando todos os produtos!".center(50))
    print(50 * "-")

    time.sleep(1)

    itens = LocadoraDoCarlao.listarItens()

    if not itens:
        print("Nenhum item cadastrado.")
    else:
        for i, item in enumerate(itens, start=1):
            tipo = "Jogo" if isinstance(item, Jogos) else "Filme"
            status = "Disponível" if item.getDisponivel() else "Indisponível"
            
            # Mostrar mais informações dependendo do tipo
            if tipo == "Jogo":
                print(f"{i}. [Jogo] {item.getTitulo()} | Plataforma: {item._Jogos__plataforma} | Faixa Etária: {item._Jogos__faixaEtaria} | {status}")
            else:
                print(f"{i}. [Filme] {item.getTitulo()} | Gênero: {item._Filmes__genero} | Duração: {item._Filmes__duracao} min | {status}")


def emprestar_devolver():
    os.system("cls")
    print(50 * "-")
    print("Emprestar/Devolver Itens".center(50))
    print(50 * "-")
    time.sleep(1)

    # Escolher cliente
    clientes = LocadoraDoCarlao.listarClientes()
    if not clientes:
        print("Nenhum cliente cadastrado.")
        return

    print("\nClientes cadastrados:")
    for i, c in enumerate(clientes, start=1):
        print(f"{i}. {c._Clientes__nome}")
    
    escolha_cliente = int(input("\nEscolha o cliente pelo número: ")) - 1
    cliente = clientes[escolha_cliente]

    # Escolher ação
    print("\nO que deseja fazer?")
    print("1 -> Emprestar item")
    print("2 -> Devolver item")
    acao = int(input("--> "))

    itens = LocadoraDoCarlao.listarItens()

    if acao == 1:  # Emprestar
        disponiveis = [item for item in itens if item.getDisponivel()]
        if not disponiveis:
            print("Não há itens disponíveis para empréstimo.")
            return

        print("\nItens disponíveis:")
        for i, item in enumerate(disponiveis, start=1):
            tipo = "Jogo" if isinstance(item, Jogos) else "Filme"
            print(f"{i}. [{tipo}] {item.getTitulo()}")

        escolha_item = int(input("\nEscolha o item pelo número: ")) - 1
        item_escolhido = disponiveis[escolha_item]

        # Emprestar
        cliente._Clientes__itensLocados.append(item_escolhido)
        item_escolhido.setDisponivel(False)
        print(f"\n{item_escolhido.getTitulo()} foi emprestado para {cliente._Clientes__nome}!")

    elif acao == 2:  # Devolver
        locados = cliente._Clientes__itensLocados
        if not locados:
            print(f"{cliente._Clientes__nome} não possui itens para devolver.")
            return

        print("\nItens locados pelo cliente:")
        for i, item in enumerate(locados, start=1):
            tipo = "Jogo" if isinstance(item, Jogos) else "Filme"
            print(f"{i}. [{tipo}] {item.getTitulo()}")

        escolha_item = int(input("\nEscolha o item pelo número: ")) - 1
        item_escolhido = locados.pop(escolha_item)
        item_escolhido.setDisponivel(True)
        print(f"\n{item_escolhido.getTitulo()} foi devolvido com sucesso!")







 







