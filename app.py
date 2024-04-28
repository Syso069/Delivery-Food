import os

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
            os.system('cls')
            print('Opção inválida!\n')

def cadastro_restaurante():
    os.system('cls')
    print('Cadastrar restaurante\n')

def listar_restaurante():
    os.system('cls')
    print('Listar restaurante\n')

def ativar_restaurante():
    os.system('cls')
    print('Ativar restaurante\n')

def finalizando_app(): 
    os.system('cls')
    print('Finalizando app\n')

def main(): 
    exibir_nome_do_aplicativo()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()