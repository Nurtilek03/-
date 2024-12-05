import sqlite3

class DatabaseManager():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    def close(self):
        self.conn.close()

class User(DatabaseManager):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name VARCHAR(20) NOT NULL,
            age INT DEFAULT NULL 
                   
            )

    ''')
    
    conn.commit() 
    conn.close()
        
    

    def register(self, full_name, age):
        self.full_name = full_name
        self.age = age
        full_name = input("Введите ФИО: ")
        age = int(input("Введите возрасть: "))
            
        self.cursor.execute('''
            INSERT INTO geeks (full_name, age)
            VALUES (?, ?)
        ''', (full_name, age))
        
    conn.commit() 
    conn.close()

    register('Nurtilek Ibragimov', '21')

class Admin(User):
    def __init__(self,conn):
        pass
    def delete(self,conn):
        self.conn = sqlite3.connect('users.db')
        self.cursor = conn.cursor()
        

        delete_id = int(input(': '))
        
        self.cursor.execute('''
            DELETE FROM geeks WHERE id = ?
        ''', (delete_id,))
class Costumer(User):
    def __init__(self,conn):
        pass
        
    def find(id):
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT * FROM books WHERE id = ?
        ''', (id,))

        book = cursor.fetchone()
        conn.close() 
