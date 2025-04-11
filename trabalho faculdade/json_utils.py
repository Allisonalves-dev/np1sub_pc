import json

def salvar_tarefas_em_arquivo(tarefas, nome_arquivo):
    with open(nome_arquivo, 'w') as f:
        json.dump(tarefas, f, indent=4)

def carregar_tarefas_de_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []