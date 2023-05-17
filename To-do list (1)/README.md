To-do list using Python and Pyrebase


Apresentação: Esse é um mini projeto CRUD que fiz para o teste de estágio da minha escola assim como meu primeiro projeto com Python.
              Utilizei conceitos que aprendi com os mundos de Python3 - Curso em Vídeo e conceitos aprendidos com o Google Firebase.
            


Especificações que usei:
    Python3.9.16
    pyrebase4 ou pyrebase



Instalação:
    pip install pyrebase4 ou 
    pip install pyrebase



Configuração:

    1. Criar projeto no Firebase
    
    2.Home Firebase: Adicionar um app: Web
    
    3.Adicionar o SDK do Firebase
          3- Setar as configurações do SDK em functions_to_do.py

                    firebaseConfig = {
                           "apiKey": "......",
                           "authDomain": "......",
                           "projectId": "......",
                           "storageBucket": "......",
                           "messagingSenderId": "......",
                           "appId": "......",
                           "measurementId": "......",
                           "databaseURL":"......"
                           }

    
    4.Home Firebase ---> Criação ---> Realtime Database ---> Criar banco de dados
    
    5.Iniciar modo teste
    
    6.Realtime database: Alterar regras
            6-  {
                  "rules": {
                   ".read": true,  // 2023-6-15
                   ".write": true,  // 2023-6-15
                    }
                }

          
    
    
    Fim
