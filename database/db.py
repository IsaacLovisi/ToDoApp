import sqlite3

DB_NAME = 'todo.db'

def conectar():
    return sqlite3.connect(DB_NAME)

def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tarefas(
        id INTEGER PRIMARY KEY AUTOINCREMENTE,
        tarefa TEXTO NOT NULL,
        tarefa_concluida BOOLEAN DEFAULT 0
    )""")
