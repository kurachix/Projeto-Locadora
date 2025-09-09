# Importando o conteudo do functions para o funcionamento do código a seguir
from functions import *

os.system("cls")

print(50 * "-")
print("Bem-Vindo a Locadora, iniciado o sistema!".center(50))
print(50 * "-")
time.sleep(3)

while True:
    try:
        os.system("cls")

        print(50 * "-")
        print("Bem-Vindo a Locadora, iniciado o sistema!".center(50))
        print(50 * "-")

        print("")
        print("SELECIONE A OPÇÃO QUE DESEJA")
        print("1 - CADASTRO DE CLIENTE")
        print("2 - LISTAR")
        print("3 - CADASTRO DE ITEM")
        print("4 - EMPRESTAR/DEVOLVER")
        print("0 - SAIR")
        escolha = int(input("--> "))

        match escolha:
            case 1:
                cadastro_cliente()
            case 2:
                listar_itens()
            case 3:
                cadastro_itens()
            case 4:
                emprestar_devolver()
            case 0:
                print("SAINDO...")
                os.system("pause")
                break
            case _:
                print("ESCOLHA INVALIDA")
                os.system("pause")

    except Exception as e:
        print(f"Ocorreu um erro Inesperado: {e}")
        os.system("pause")





