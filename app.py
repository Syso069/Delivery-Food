import os

restaurante = ['AiFoude', 'Hamburgui Du Zé']

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
    print('3. Ativar restaurante')
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
                ativar_restaurante()

            case 4: 
                finalizando_app()
            case _:
                opcao_invalida()
    except: 
        opcao_invalida()

def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal: ')
    main()

def cadastro_restaurante():
    exibir_subtitulo('Cadastro de restaurante\n')
    nome_do_restaurante = str(input('Digite o nome restaurante\n'))
    restaurante.append(nome_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu_principal()

def listar_restaurante():
    exibir_subtitulo('Lista de restaurante\n')
    for item in restaurante:
        print(f'.{item}')
    voltar_ao_menu_principal()

def ativar_restaurante():
    exibir_subtitulo('Ativar restaurante\n')
    voltar_ao_menu_principal()

def finalizando_app(): 
    exibir_subtitulo('Finalizando app\n')

def opcao_invalida():
    exibir_subtitulo('Opção inválida!\n')
    voltar_ao_menu_principal()

def main(): 
    os.system('cls')
    exibir_nome_do_aplicativo()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()