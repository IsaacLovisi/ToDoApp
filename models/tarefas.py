from dataclasses import dataclass 
from database.db import conectar

@dataclass
class Tarefa:
    id: int
    nome: str
    descricao: str
    prioridade: int
    status: bool

    @staticmethod
    def criar(nome, descricao, prioridade):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tarefas (nome, descricao, prioridade) VALUES (?, ?, ?)", (nome, descricao, prioridade))
        conn.commit()
        conn.close()

    def marcar_concluida(id):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("UPDATE tarefas SET status = 1 WHERE id = ?",(id,))
        conn.commit()
        conn.close()

    def visualizar_tarefas() -> list:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tarefas")
        lista = cursor.fetchall()
        ver = input("1- Ver por prioridade\n2- Ver por ordem de criação\n")
        if ver == "1": 
            lista.sort(reverse=True, key=lambda x: x[4])
        elif ver != "2":
            print("Digite uma opção válida")
        for tarefa in lista: 
            print(f"\nid: {tarefa[0]}\nnome: {tarefa[1]}\nstatus: {tarefa[2]}\ndescricao: {tarefa[3]}\nprioridade: {tarefa[4]}\n\n")
        conn.commit()
        conn.close()
        return [list(tarefa) for tarefa in lista]  


    
    