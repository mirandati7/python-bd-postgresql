from cadastro_categoria import menu_categoria
from cadastro_produto import menu_produto
from conexao import conecta_db


def login(conexao) -> None:
   login =  input("Digite o login:")
   senha =  input("Digite a senha:")

   cursor = conexao.cursor()
   cursor.execute(" select id,login,senha from usuario " +
                  " where login = %s and senha = %s",(login,senha) )
   registro = cursor.fetchone()

   if registro is None:
       print("Usuario e senhas invalidos")
   else:
        menu_principal()


def menu_principal():
    print("|--------------------------------|")
    print("|       Menu -> Programa         |")
    print("|--------------------------------|")
    print("|     1 - Categoria              |")
    print("|     2 - Produto                |")
    print("|     3 - Cliente                |")
    print("|     4 - Venda                  |")
    print("|     5 - Sair do Sistema        |")
    print("|--------------------------------|")

    while True:
        opcao = input("Escolha uma opção:")

        if opcao == "1":
            menu_categoria(opcao)
        elif opcao == "2":
            menu_produto(opcao)
        elif opcao == "3":
            print("Ainda não foi implementado")
        elif opcao == "4":
            print("Ainda não foi implementado")
        elif opcao == "5":
            break
        else:
            print("Opção invalida, tente novamente")



if __name__ == "__main__":
    conexao = conecta_db()
    login(conexao)