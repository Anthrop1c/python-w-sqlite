import sqlite3

class Database:
    def __init__(self):
        self.connection = sqlite3.connect('database.db') #Crianddo o banco e designando o nome.
        self.cursor = self.connection.cursor()
        self.createTable()
    
    def createTable(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS people (name text,age integer, email text)") #Criando a tabela people
        self.connection.commit()