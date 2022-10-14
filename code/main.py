#!/usr/bin/env python3

from ast import main
from select import select
from database import Database


def main():
  print("\n    BEM VINDO ")
  
  database = Database() #instanciando o banco

  select = 0
  while select != 5:
    print('''    Escolha a sua opção abaixo! \n
    [1] Adicionar novo registro
    [2] Editar registro existente
    [3] Deletar registro permanente
    [4] Exportar database em txt
    [5] Sair do programa''')
    
    select = int(input(''))
    if select == 1:
      import addMenu
    elif select == 2:
      import editMenu
    elif select == 3:
      import deleteMenu
    elif select == 4:
      database.cursor.execute("SELECT * FROM people") #percorre o banco de dados
      rows = database.cursor.fetchall()
      with open ("database.txt","w") as arquivo:
          arquivo.write('Todos os registros:')  
      for row in rows: #percorre os dados retornados e escreve em um arquivo txt
        with open ("database.txt","a") as arquivo:
          arquivo.write(f'\n{row}')
      print('Salvo com sucesso! \n') 
    elif select == 5:
      exit('Finalizando...')  
    else:
      print ('Escolha uma opção válida!')  

  database.connection.commit()
  database.connection.close()
main()  
