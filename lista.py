produtos = {}

# Função para salvar a lista em um arquivo
def salvar_lista(nome_arquivo='lista_compras.txt'):
    with open(nome_arquivo, 'w') as file:
        for produto in produtos:
            file.write(f'{produto}\n')

def adicionar_contato(nome, quantidade):
    # Verificar se o produto existe
    produtos[nome] = quantidade

def visualizar_produtos():
    if not produtos:
        print('Nenhum produto encontrado')
    else:
        for nome, quantidade in produtos.items():
            print(f'{nome}: {quantidade}')

def excluir_produto(nome):
    if nome in produtos:
        del produtos[nome]  # Verificando se o nome existe na lista
        print(f'Produto {nome} excluído com sucesso!') 
    else:
        print(f'Produto {nome} não encontrado')

def atualizar_produto(nome, nova_quant):
    if nome in produtos:
        produtos[nome] = nova_quant
        print('Produto atualizado!')
    else:
        print('Produto não existe')

def buscar_produto(nome):
    if nome in produtos:
        print(f'Nome: {nome}')
        print(f'Quantidade: {produtos[nome]}')
    else:
        print('Produto não existe')

def menu():
    while True:
        print('\nMENU')
        print('1. Adicionar produto')
        print('2. Visualizar produtos')
        print('3. Buscar produto')
        print('4. Atualizar produto')
        print('5. Excluir produto')
        print('6. Sair e Salvar Lista')
        
        escolha = input('Escolha uma opção (1-6): ')

        if escolha == '1':
           nome = input('Insira o nome: ')
           quantidade = input('Insira a quantidade: ')
           adicionar_contato(nome, quantidade)

        elif escolha == '2':
            visualizar_produtos()
           
        elif escolha == '3':
            nome = input('Informe o nome do produto que deseja buscar: ')
            buscar_produto(nome)

        elif escolha == '4':
            nome = input('Informe o nome do produto que deseja atualizar: ')
            nova_quant = input('Informe a nova quantidade: ')
            atualizar_produto(nome, nova_quant)

        elif escolha == '5':
            nome = input('Insira o nome do produto a ser excluído: ')
            excluir_produto(nome)

        elif escolha == '6':
            salvar_lista()
            print('Saindo do Programa')
            break

        else:
            print('\nOpção inválida. Por favor, escolha uma opção de 1 a 6.')

menu()