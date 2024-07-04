from conexao import conecta_db


def consultar(conexao):
    cursor = conexao.cursor()
    # Execução do Select no banco de dados
    cursor.execute("select id,nome from cliente")
    # Recuperar os registros
    registros = cursor.fetchall()
    print("|-----------------------------------|")
    for registro in registros:
        print(f"| ID ..:  {registro[0]}   - Nome ..:   {registro[1]}")
        print("|-----------------------------------|")

def inserir(conexao):
    cursor = conexao.cursor()
    nome_cliente = input('Digite o nome do cliente: ') 
    sql_insert = "insert into cliente (nome) values ('"+ nome_cliente +  "')"
    cursor.execute(sql_insert)
    conexao.commit()
        
def alterar(conexao):
    cursor = conexao.cursor()
    id = input("Digite o ID: ")
    nome_cliente = input('Digite o nome do Cliente: ')
    sql_update = "update cliente set nome ='" + nome_cliente + "' where id = " + id
    cursor.execute(sql_update)
    conexao.commit()


def deletar(conexao):
    cursor = conexao.cursor()
    id = input("Digite o ID: ")
    sql_delete = "delete from  cliente where id = " + id
    cursor.execute(sql_delete)
    conexao.commit()

def menu_cliente(opcao):
    print("|--------------------------------|")
    print("|       Menu -> Cliente        |")
    print("|--------------------------------|")
    print("|     1 - Consultar Cliente    |")
    print("|     2 - Inserir Cliente      |")
    print("|     3 - Alterar Cliente      |")
    print("|     4 - Deletar Cliente      |")
    print("|     5 - Sair do Sistema        |")
    print("|--------------------------------|")

    conexao = conecta_db()

    while True:
        opcao = input("Escolha uma opção:")

        if opcao == "1":
            consultar(conexao)
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