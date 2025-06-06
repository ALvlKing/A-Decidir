#1. Adicionar Tarefa
def adicionar_tarefas():
    '''Abre o arquivo da lista de tarefas e escreve as atividades do usuário em um documento txt'''
    with open('list_tarefas.txt', 'a') as listat:
        tarefa = input('Digite sua Tarefa:\n')
        listat.write(tarefa + '\n')

#----------------------------------------------------------------------------------------------------------------------
#2. Ver Tarefas
def todas_tarefas():
    '''Abre o arquivo com as tarefas e mostra ao usuário'''
    with open('list_tarefas.txt', 'r') as listat:
        total = listat.read()
        print('\nEssas são suas tarefas:')
        print(total)
        print('Já finalizou alguma hoje? Vamos dar o nosso melhor! 😄')

#----------------------------------------------------------------------------------------------------------------------
#3. Marcar tarefa como concluída - versão simples
def marcar_tarefa():
    arquivo = open('list_tarefas.txt', 'r')
    tarefas = arquivo.readlines()
    arquivo.close()

    if len(tarefas) == 0:
        print("Não há tarefas para marcar.")
        return

    for i in range(len(tarefas)):
        print(f"{i+1}. {tarefas[i].strip()}")

    num = int(input("Número da tarefa para marcar como concluída: ")) - 1

    if num < 0 or num >= len(tarefas):
        print("Número inválido.")
        return

    if "[CONCLUÍDA]" in tarefas[num]:
        print("Essa tarefa já está marcada como concluída.")
    else:
        tarefas[num] = tarefas[num].strip() + " [CONCLUÍDA]\n"

        arquivo = open('list_tarefas.txt', 'w')
        arquivo.writelines(tarefas)
        arquivo.close()

        print("Tarefa marcada como concluída!")

#----------------------------------------------------------------------------------------------------------------------
#4. Remover Tarefas
def remover_tarefas():
    arquivo = "list_tarefas.txt"
    '''Seleciona o texto a ser deletado'''
    print("Digite parte do conteúdo da linha que deseja excluir:")
    texto = input()
    '''Abre o arquivo e lê todas as linhas'''
    abrido = open(arquivo, "r")
    linhas = abrido.readlines()
    abrido.close()
    '''Mostra as linhas que contêm o texto'''
    for i in range(len(linhas)):
        if texto in linhas[i]:
            print(i, ":", linhas[i].strip())
    '''Pede o número da linha a remover'''
    print("Digite o número da linha que deseja remover:")
    num = int(input())
    '''Remove a linha escolhida'''
    del linhas[num]
    '''Reescreve o arquivo'''
    abrido = open(arquivo, "w")
    abrido.writelines(linhas)
    abrido.close()

    print("Linha removida com sucesso.")

#----------------------------------------------------------------------------------------------------------------------
def menu():
    while True:
        print("\n=== MENU DE TAREFAS ===")
        print("1 - Adicionar tarefa")
        print("2 - Listar tarefas")
        print("3 - Marcar tarefa como concluída")
        print("4 - Excluir tarefa")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_tarefas()
        elif opcao == "2":
            todas_tarefas()
        elif opcao == "3":
            marcar_tarefa()
        elif opcao == "4":
            remover_tarefas()
        elif opcao == "5":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()
