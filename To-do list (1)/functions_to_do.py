import pyrebase 
from interface import cabeçalho
from time import sleep

#Configuração

firebaseConfig = {
 #Insira a configuração do SDK
}


#Inicialização
firebase = pyrebase.initialize_app(firebaseConfig)

#Banco de dados
db = firebase.database()

#Dados necessários
dados_tarefa = {'nome_tarefa':'','categoria':''}



def criarTarefa():
    cabeçalho('\nCriando tarefa...')
    
    tarefa = str(input('Digite o nome da nova tarefa: '))
    

    if tarefa.strip() == '':
        print('O campo tarefa não pode ser vazio: ')

    else:
        try:
            db.child('Tarefas').child(tarefa).set({'tarefa':tarefa,'categoria':'To-do'})

        except:
            print('Não foi possível criar tarefa\n')

        else:
            print('Tarefa criada com sucesso!\n')
        


def listarTarefas():
    cabeçalho('\nMostrar tarefas')

    tarefas = db.child("Tarefas").get()

    #Lista as tarefas existentes
    for tarefa in tarefas.each():
        print(f'▶{tarefa.key()}')
        print(f'  ↪{tarefa.val().get("categoria")}')



def atualizarTarefa():
    listarTarefas()
    cabeçalho('\nAtualizar tarefa:')

    tarefas_salvas = db.child("Tarefas").get()
    lista_tarefas = []

    #Cria uma lista das tarefas existentes e verifica
    for tarefa_salva in tarefas_salvas.each():
        lista_tarefas.append(tarefa_salva.key())


    #Tarefa a ser atualizada
    tarefa = str(input('Digite o nome da tarefa: '))
    categoria = str(input('Alterar categoria para: '))


    if tarefa not in lista_tarefas:
        print('A tarefa mencionada não está cadastrada...')

    else:
        try:    
            if tarefa.strip() and categoria.strip() != '':
                db.child('Tarefas').child(tarefa).update({'categoria':categoria})
        
        except:
            print('Erro para atualizar tarefa...')
            sleep(1.2)
            
        else:
            print('Tarefa alterada com sucesso!')

    
    

def apagarTarefa():

    listarTarefas()
    cabeçalho('\nDeletar tarefa:')

    tarefas_salvas = db.child("Tarefas").get()
    lista_tarefas = []

    #Cria uma lista das tarefas existentes e verifica
    for tarefa_salva in tarefas_salvas.each():
        lista_tarefas.append(tarefa_salva.key())


    #Tarefa a ser apagada
    tarefa = str(input('Digite o nome da tarefa: ')).strip()


    if tarefa not in lista_tarefas:
        print('Não é possível apagar a tarefa: Não está cadastrada')

    else:
        try:
            db.child('Tarefas').child(tarefa).remove()
            
        except:
            print('Erro ao deletar sua tarefa... Tente novamente.')
            sleep(1.2)
            
        else:
            print(f'Tarefa {tarefa} apagada com sucesso!')
        
        
