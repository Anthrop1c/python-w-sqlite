from mailbox import NotEmptyError
import sqlite3 #importando o sqlite
from tkinter import INSERT  
from database import Database

def AddMenu():
  try:
    name= input('Digite seu nome: ') #pedindo ao usuário que coloque seus dados
    age = input('Digite a sua idade: ')
    email = input('Digite seu email: ')

    database = Database()
    database.cursor.execute("INSERT INTO people VALUES('"+name+"',"+age+",'"+email+"')") #Inserindo os primeiros registros no database.connection
    database.connection.commit()

    print("\n REGISTRADO COM SUCESSO! \n")
  except sqlite3.Error as error:
    print("Erro ao registrar!",error)
AddMenu()