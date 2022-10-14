from database import Database

class PeopleEditor:
  def __init__(self):
    self.database = Database()    

  def editemail(self):
    self.database.cursor.execute("SELECT * FROM people")

    print('Todos os registros são:') #mostrando os registros da minha tabela
    for row in self.database.cursor.fetchall():
      print(row)

    editedEmail = input('Digite o email a ser modificado: ')
    nEmail = input('Digite o novo email: ')

    self.database.cursor.execute("UPDATE people SET email = '"+nEmail+"' WHERE email = '"+editedEmail+"'")  
    self.database.cursor.execute("SELECT * FROM people")
    print('Registros atualizados:', self.database.cursor.fetchall()) #mostrando os registros da minha tabela

    self.database.connection.commit()



  def editage(self):
    self.database.cursor.execute("SELECT * FROM people")

    print('Todos os registros são:') #mostrando os registros da minha tabela
    for row in self.database.cursor.fetchall():
      print(row)

    editedage = input('Digite a idade a ser modificada: ')
    nage = input('Digite a nova idade: ')

    self.database.cursor.execute("UPDATE people SET age = '"+nage+"' WHERE age = '"+editedage+"'")
    self.database.cursor.execute("SELECT * FROM people")
    print('Registros atualizados:',self.database.cursor.fetchall()) #mostrando os registros da minha tabela

    self.database.connection.commit()



  def editname(self):
    self.database.cursor.execute("SELECT * FROM people")

    print('Todos os registros são:') #mostrando os registros da minha tabela
    for row in self.database.cursor.fetchall():
      print(row)

    editedname = input('Digite o nome a ser modificado: ')
    nname = input('Digite o novo nome: ')

    self.database.cursor.execute("UPDATE people SET name = '"+nname+"' WHERE name = '"+editedname+"'")
    self.database.cursor.execute("SELECT * FROM people")
    print('Registros atualizados:', self.database.cursor.fetchall()) #mostrando os registros da minha tabela

    self.database.connection.commit()