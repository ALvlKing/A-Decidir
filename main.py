import json
# Menu de Seleção



# 1. Adicionar Tarefas
try:
    with open("tarefas.json", "r") as f:
        lista_tarefa = json.load(f)
except FileNotFoundError:
    lista_tarefa = []


while True:
    nova_tarefa = input('Digite sua tarefa ou "sair" para terminar: ')

    if nova_tarefa.lower() == 'sair':
        break

    lista_tarefa.append(nova_tarefa)

    with open("tarefas.json", "w") as f:
        json.dump(lista_tarefa, f, indent=4)

    print("\nTarefas atualizadas:")
    for tarefa in lista_tarefa:
        print(f"- {tarefa}")

print("\nTarefas salvas com sucesso.")

# 3. Marcar Tarefas




# 4. Excluir Tarefas
