from time import sleep


def cabeçalho(prompt='',tam=42):
    print('-'*tam)
    print(prompt)
    print('-'*tam)



def leiaInt(prompt=''):

    while True:
        try:
            n = int(input(f'{prompt}'))
        

        except (ValueError,TypeError):
            print('Erro!! Digite um número inteiro!')


        except (KeyboardInterrupt):
            print('Entrada de dados interrompida...')
            return 0


        else:
            break

    return n



def Menu(opc):
    from functions_to_do import criarTarefa,listarTarefas,atualizarTarefa,apagarTarefa
    
    while True:    
        print('\n')
        cabeçalho('To-do list'.center(42))

        for c,item in enumerate(opc):
            print(f'{c+1} - {item}')
            
        
        print('-'*42)
        option = leiaInt('Digite a opção: ')

        if option == 1:
            sleep(1.5)
            criarTarefa()
    
        elif option == 2:
            sleep(1.5)
            listarTarefas()
    
        elif option == 3:
            sleep(1.5)
            atualizarTarefa()
    
        elif option == 4:
            sleep(1.5)
            apagarTarefa()
    
        elif option == 5:
            cabeçalho('Encerrando...')
            break
        
        else:
            print('Digite uma opção válida!\n')

        sleep(1.5)

        