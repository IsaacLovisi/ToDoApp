from database.db import conectar, criar_tabela
from models.tarefas import Tarefa




Tarefa.marcar_concluida(22)
visualizar = Tarefa.visualizar_tarefas()
tarefa = next((t for t in visualizar if t[0] == 22), None)
print(tarefa)