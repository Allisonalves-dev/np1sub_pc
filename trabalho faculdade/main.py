import requests
import json
from json_utils import salvar_tarefas_em_arquivo, carregar_tarefas_de_arquivo
from tarefas import cadastrar_tarefa, listar_tarefas, buscar_tarefas_por_status, buscar_tarefas_por_nome, atualizar_status_tarefa, remover_tarefa

GITHUB_JSON_URL = "https://raw.githubusercontent.com/Allisonalves-dev/np1sub_pc/refs/heads/main/tarefas.json" 
TAREFAS = []
NOME_ARQUIVO_LOCAL = "tarefas.json"

def carregar_tarefas_do_github():
    global TAREFAS
    print("Tentando carregar tarefas do GitHub...")  
    try:
        response = requests.get(GITHUB_JSON_URL)
        response.raise_for_status()
        data = response.json()
        print("Carregamento do GitHub bem-sucedido. Dados recebidos:")  
        print(data) 
        TAREFAS = data
        print("Tarefas carregadas do GitHub com sucesso!")
    except requests.exceptions.RequestException as e:
        print(f"Erro ao carregar tarefas do GitHub: {e}")
        TAREFAS = carregar_tarefas_de_arquivo(NOME_ARQUIVO_LOCAL)
        if not TAREFAS:
            TAREFAS = []
        print("Tarefas carregadas do arquivo local.")  
    except json.JSONDecodeError as e:
        print(f"Erro ao decodificar JSON do GitHub: {e}")
        TAREFAS = carregar_tarefas_de_arquivo(NOME_ARQUIVO_LOCAL)
        if not TAREFAS:
            TAREFAS = []
        print("Tarefas carregadas do arquivo local.") 

def exibir_menu():
    print("\nMenu de opções:")
    print("1. Cadastrar Tarefa")
    print("2. Listar Tarefas")
    print("3. Buscar Tarefa por Status")
    print("4. Buscar Tarefa por Nome")
    print("5. Atualizar Status de Tarefa")
    print("6. Remover Tarefa")
    print("7. Sair")

def cadastrar():
    descricao = input("Descrição da tarefa: ")
    status = input("Status (pendente, em andamento, concluída): ")
    prazo = input("Prazo de conclusão: ")
    global TAREFAS
    TAREFAS = cadastrar_tarefa(TAREFAS, descricao, status, prazo)
    salvar_tarefas_em_arquivo(TAREFAS, NOME_ARQUIVO_LOCAL)

def listar():
    carregar_tarefas_do_github()  
    if not TAREFAS:
        print("Não há tarefas cadastradas.")
        return
    for tarefa in TAREFAS:
        print(f"Descrição: {tarefa['descricao']} | Status: {tarefa['status']} | Prazo: {tarefa['prazo']}")

def buscar_por_status():
    carregar_tarefas_do_github()  
    status = input("Digite o status para buscar: ")
    resultados = buscar_tarefas_por_status(TAREFAS, status)
    if not resultados:
        print("Nenhuma tarefa encontrada com esse status.")
        return
    for tarefa in resultados:
        print(f"Descrição: {tarefa['descricao']} | Status: {tarefa['status']} | Prazo: {tarefa['prazo']}")

def buscar_por_nome():
    carregar_tarefas_do_github()  # Carrega do GitHub antes de buscar
    nome = input("Digite o nome da tarefa para buscar: ")
    resultados = buscar_tarefas_por_nome(TAREFAS, nome)
    if not resultados:
        print("Nenhuma tarefa encontrada com esse nome.")
        return
    for tarefa in resultados:
        print(f"Descrição: {tarefa['descricao']} | Status: {tarefa['status']} | Prazo: {tarefa['prazo']}")

def atualizar_status():
    """Atualiza o status de uma tarefa."""
    descricao = input("Descrição da tarefa para atualizar: ")
    novo_status = input("Novo status: ")
    global TAREFAS
    if atualizar_status_tarefa(TAREFAS, descricao, novo_status):
        salvar_tarefas_em_arquivo(TAREFAS, NOME_ARQUIVO_LOCAL)
        print("Status atualizado com sucesso!")
    else:
        print("Tarefa não encontrada.")

def remover():
    """Remove uma tarefa."""
    descricao = input("Descrição da tarefa para remover: ")
    global TAREFAS
    TAREFAS[:] = remover_tarefa(TAREFAS, descricao)
    salvar_tarefas_em_arquivo(TAREFAS, NOME_ARQUIVO_LOCAL)
    print("Tarefa removida com sucesso!")

if __name__ == "__main__":
    carregar_tarefas_do_github() 
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar()
        elif opcao == '2':
            listar()
        elif opcao == '3':
            buscar_por_status()
        elif opcao == '4':
            buscar_por_nome()
        elif opcao == '5':
            atualizar_status()
        elif opcao == '6':
            remover()
        elif opcao == '7':
            break
        else:
            print("Opção inválida.")