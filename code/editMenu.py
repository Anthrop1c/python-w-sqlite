from dataclasses import dataclass
from database import Database
from peopleEditor import PeopleEditor

def EditMenu():
  peopleEditor = PeopleEditor()
  database = Database()

  c = 0
  while c != 4:
    print ('''    Escolha uma das opções abaixo:
    [1] Editar nome
    [2] Editar idade
    [3] Editar email
    [4] Sair do menu''')

    c = int(input('     '))
    if c == 1:
     peopleEditor.editname()
    elif c == 2:
     peopleEditor.editage()
    elif c == 3:
     peopleEditor.editemail()
    elif c == 4:
      print('Saindo...')
    else:
      print('Escolha uma opção válida')

  database.connection.commit()
  database.connection.close()
EditMenu()
