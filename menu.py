from cadastro_categoria import (alterar, consultar, deletar, inserir,
                                menu_categoria)
from conexao import conecta_db

if __name__ == "__main__":
    print("|--------------------------------|")
    print("|       Menu -> Programa         |")
    print("|--------------------------------|")
    print("|     1 - Categoria              |")
    print("|     2 - Produto                |")
    print("|     3 - Cliente                |")
    print("|     4 - Venda                  |")
    print("|     5 - Sair do Sistema        |")
    print("|--------------------------------|")

    conexao = conecta_db()

    while True:
        opcao = input("Escolha uma opção:")

        if opcao == "1":
            menu_categoria(opcao)
        elif opcao == "2":
            inserir(conexao)
        elif opcao == "3":
            alterar(conexao)
        elif opcao == "4":
           deletar(conexao)
        elif opcao == "5":
            break
        else:
            print("Opção invalida, tente novamente")