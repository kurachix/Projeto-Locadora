# Importando o conteudo do functions para o funcionamento do código a seguir
from functions import *

os.system("cls")

print(50 * "-")
print("Bem-Vindo a Locadora, iniciado o sistema!".center(50))
print(50 * "-")
time.sleep(3)

cadastro_cliente()
cadastro_itens()
emprestar_devolver()


os.system("pause")
listar_itens()




