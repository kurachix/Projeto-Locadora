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
            
            codigo = input("Adi")
            titulo = 
            plataforma = 
            faixaEtaria = 
            
            
            
            os.system("cls")
            LocadoraDoCarlao.cadastroJogo(codigo=codigo, titulo=titulo, plataforma=plataforma, faixaEtaria=faixaEtaria)
            
            os.system("cls")
            print("Jogo adicionado com sucesso, verifique na lista de jogos")
            while True:
 







