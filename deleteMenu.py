from database import Database

def DeleteMenu():
    database = Database()
    
    print ("Qual registro deseja excluir?")

    database.cursor.execute("SELECT * FROM people")
    print(database.cursor.fetchall()) #mostrando os registros da minha tabela

    delete = input('DIGITE O NOME: ') #solicitando o usuário qual idade deseja remover
  
    database.cursor.execute("DELETE from people WHERE name = '"+delete+"'") #designando o dado que irá ser deletado

    print('Fim da operação \n')

    database.connection.commit()
DeleteMenu()