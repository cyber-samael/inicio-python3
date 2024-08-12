import os

restaurantes = ['Kamp','Pizza'] 

def exibir_nome_programa():
    print (' \nSabor Express\n ')

def exibir_opcoes():
    
    print ('1. Cadastrar restaurante')
    print ('2. Listar Restaurantes')
    print ('3. Ativar Restaurante')
    print ('4. Sair')

def finalizar_app():
    print (' Finalizando... ')
    os.system('cls')

def cadastrar_novo_restaurante():
    os.system('cls')
    print('Cadastro de novos Restaurantes\n')
    nome_do_restaurante = input('Digite o nome do restaurante: ')
    restaurantes.append(nome_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso')
    voltar_ao_menu()
    
def listar_restaurantes():
     os.system('cls')
     print('Listando restaurantes\n')
     for restaurante in restaurantes:
      print(f'-{restaurante}')
     voltar_ao_menu()

def voltar_ao_menu():
    input ('\nDigite qualquer tecla para voltar ao menu ')
    main()


def opcao_invalida():
     print ('Opção Invalida\n ')
     voltar_ao_menu()


def escolher_opcao():
    try:
        opcao_escolhida = int(input ('Escolha uma opção: '))
    # opcao_escolhida = int (opcao_escolhida)


        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            print (' Ativar Restaurante. ')
        elif opcao_escolhida == 4:
            finalizar_app()
                
        else :
            opcao_invalida()
    
    except: opcao_invalida()

def main():
        os.system('cls')
        exibir_nome_programa()
        exibir_opcoes()
        escolher_opcao()

if __name__ == '__main__':
        main()