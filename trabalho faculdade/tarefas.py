def cadastrar_tarefa(tarefas, descricao, status, prazo):
    tarefa = {"descricao": descricao, "status": status, "prazo": prazo}
    tarefas.append(tarefa)
    return tarefas

def listar_tarefas(tarefas):
    return tarefas

def buscar_tarefas_por_status(tarefas, status):
    return [tarefa for tarefa in tarefas if tarefa['status'].lower() == status.lower()]

def buscar_tarefas_por_nome(tarefas, nome):
    return [tarefa for tarefa in tarefas if nome.lower() in tarefa['descricao'].lower()]

def atualizar_status_tarefa(tarefas, descricao, novo_status):
    for tarefa in tarefas:
        if tarefa['descricao'].lower() == descricao.lower():
            tarefa['status'] = novo_status
            return True
    return False

def remover_tarefa(tarefas, descricao):
    return [tarefa for tarefa in tarefas if tarefa['descricao'].lower() != descricao.lower()]