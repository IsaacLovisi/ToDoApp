import sqlite3

DB_NAME = 'todo.db'

def conectar():
    return sqlite3.connect(DB_NAME)

def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tarefas(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXTO NOT NULL,
        status BOOLEAN DEFAULT 0,
        descricao TEXT NOT NULL, 
        prioridade INT NOT NULL
    )""")


criar_tabela()