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



 







