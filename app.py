import os

restaurantes = [{'nome': 'Aí FoudE', 'categoria': 'Bebida', 'ativo': True}, {'nome': 'GastroFude', 'categoria': 'FastFude', 'ativo': False}, 
               {'nome': 'HamBuguiU', 'categoria': 'Hamburguer', 'ativo': True}]

def exibir_nome_do_aplicativo():
    print('''
░█████╗░██╗  ███████╗░█████╗░██████╗░███████╗
██╔══██╗██║  ██╔════╝██╔══██╗██╔══██╗██╔════╝
███████║██║  █████╗░░██║░░██║██║░░██║█████╗░░
██╔══██║██║  ██╔══╝░░██║░░██║██║░░██║██╔══╝░░
██║░░██║██║  ██║░░░░░╚█████╔╝██████╔╝███████╗
╚═╝░░╚═╝╚═╝  ╚═╝░░░░░░╚════╝░╚═════╝░╚══════╝ \n''')

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alterar o estado do restaurante')
    print('4. Sair\n')

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        match opcao_escolhida:
            case 1:
                cadastro_restaurante()

            case 2:
                listar_restaurante()

            case 3: 
                alterar_estado_restaurante()

            case 4: 
                finalizando_app()
            case _:
                opcao_invalida()
    except: 
        opcao_invalida()

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * (len(texto))
    print(f'{linha}')
    print(texto)
    print(f'{linha}\n')

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal: ')
    main()

def cadastro_restaurante():
    '''
        Essa função é responsável por cadastrar novos restaurantes

        Input:
            -Nome do restaurante 
            -Categoria 
        Output:
            - Adiciona dados do restaurante ao dicionário de restaurantes 
    '''
    exibir_subtitulo('Cadastro de restaurante')
    nome_do_restaurante = str(input('Digite o nome restaurante: '))
    categoria_do_restaurante = str(input(f'Digite a categoria do {nome_do_restaurante}: '))
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria_do_restaurante, 'ativo': False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {dados_do_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu_principal()

def listar_restaurante():
    '''
    Essa função é responsável por listar todos os restaurantes cadastrados

    Output:
        - Exibe na tela a lista de restaurantes que estão ativados e desativados
    '''
    exibir_subtitulo('Lista de restaurante')
    print(f'{'Nome do restaurante'.ljust(22)} |{ 'Categoria'.ljust(22)}| Status\n')
    
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
    voltar_ao_menu_principal()

def alterar_estado_restaurante():
    '''
    Essa função é responsável por alterar o estado ativado/desativado de um restaurante

    Output:
        - Exibe mensagem na tela indicando o sucesso da operação
    '''
    exibir_subtitulo('Alterando o estado do restaurante')
    nome_restaurante = str(input('Digite o nome do restaurante que deseja alterar o estado: '))
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante ['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso!' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso!'
            print(mensagem)

    if not restaurante_encontrado:
        print(f'O restaurante {nome_restaurante} não foi encontrado')

    voltar_ao_menu_principal()

def finalizando_app(): 
    exibir_subtitulo('Finalizando app')

def opcao_invalida():
    exibir_subtitulo('Opção inválida!')
    voltar_ao_menu_principal()

def main(): 
    '''
    Função que inicia o programa 
    '''
    os.system('cls')
    exibir_nome_do_aplicativo()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()