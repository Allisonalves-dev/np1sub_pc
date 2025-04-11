def cadastrar_tarefa(tarefas, descricao, status, prazo):
    """Cadastra uma nova tarefa."""
    tarefa = {"descricao": descricao, "status": status, "prazo": prazo}
    tarefas.append(tarefa)
    return tarefas

def listar_tarefas(tarefas):
    """Lista todas as tarefas."""
    return tarefas

def buscar_tarefas_por_status(tarefas, status):
    """Busca tarefas por status."""
    return [tarefa for tarefa in tarefas if tarefa['status'].lower() == status.lower()]

def buscar_tarefas_por_nome(tarefas, nome):
    """Busca tarefas por nome (descrição)."""
    return [tarefa for tarefa in tarefas if nome.lower() in tarefa['descricao'].lower()]

def atualizar_status_tarefa(tarefas, descricao, novo_status):
    """Atualiza o status de uma tarefa."""
    for tarefa in tarefas:
        if tarefa['descricao'].lower() == descricao.lower():
            tarefa['status'] = novo_status
            return True
    return False

def remover_tarefa(tarefas, descricao):
    """Remove uma tarefa."""
    return [tarefa for tarefa in tarefas if tarefa['descricao'].lower() != descricao.lower()]