# Mensagem de boas-vindas
print('='*40)
print(' '*7 + 'BEM-VINDO A LOJA DE LIVRO KAUÃ SAMUEL')
print('='*40)

# Lista de livros e variável global para o ID
lista_livro = []
id_global = 0

# Função para cadastrar um livro na lista de livros
def cadastrar_livro(id):
    print("\n=== CADASTRAR LIVRO ===")
    nome = input("Digite o nome do livro: ")
    autor = input("Digite o autor do livro: ")
    editora = input("Digite a editora do livro: ")
    livro = {'id': id, 'nome': nome, 'autor': autor, 'editora': editora}
    lista_livro.append(livro)
    print("Livro cadastrado com sucesso!")

# Função para consultar livros
def consultar_livro():
    while True:
        print("\n=== CONSULTAR LIVRO ===")
        print("Escolha uma opção:")
        print("1. Consultar Todos")
        print("2. Consultar por Id")
        print("3. Consultar por Autor")
        print("4. Retornar ao menu")
        opcao = input("Digite o número da opção desejada: ")
        if opcao == '1':
            print("\n=== CONSULTAR TODOS OS LIVROS ===")
            if lista_livro:
                for livro in lista_livro:
                    print(livro)
            else:
                print("Nenhum livro cadastrado.")
        elif opcao == '2':
            id_busca = int(input("Digite o ID do livro: "))
            encontrado = False
            for livro in lista_livro:
                if livro['id'] == id_busca:
                    print("\n=== CONSULTAR LIVRO POR ID ===")
                    print(livro)
                    encontrado = True
                    break
            if not encontrado:
                print("Livro não encontrado.")
        elif opcao == '3':
            autor_busca = input("Digite o nome do autor: ")
            encontrados = []
            for livro in lista_livro:
                if livro['autor'] == autor_busca:
                    encontrados.append(livro)
            if encontrados:
                print("\n=== CONSULTAR LIVRO(S) POR AUTOR ===")
                for livro in encontrados:
                    print(livro)
            else:
                print("Nenhum livro encontrado para esse autor.")
        elif opcao == '4':
            break
        else:
            print("Opção inválida.")

# Função para remover livro
def remover_livro():
    while True:
        print("\n=== REMOVER LIVRO ===")
        id_remover = int(input("Digite o ID do livro a ser removido: "))
        encontrado = False
        for livro in lista_livro:
            if livro['id'] == id_remover:
                lista_livro.remove(livro)
                print("Livro removido com sucesso!")
                encontrado = True
                break
        if not encontrado:
            print("ID inválido. Livro não encontrado.")

# Menu principal
while True:
    print("\n=== MENU ===")
    print("1. Cadastrar Livro")
    print("2. Consultar Livro")
    print("3. Remover Livro")
    print("4. Encerrar Programa")
    opcao_menu = input("Digite o número da opção desejada: ")
    if opcao_menu == '1':
        id_global += 1
        cadastrar_livro(id_global)
    elif opcao_menu == '2':
        consultar_livro()
    elif opcao_menu == '3':
        remover_livro()
    elif opcao_menu == '4':
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida.")