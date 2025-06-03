#1. Adiconar Tarefa
def adicionar_tarefas():
    '''Abre o arquivo da lista de tarefas e escreve as atividades do usario em um documento txt'''
    with open('list_tarefas.txt', 'a') as listat:
        tarefa = input('Digite sua Tarefa:\n')
        listat.write    (tarefa + '\n')

#----------------------------------------------------------------------------------------------------------------------
#2. Ver Tarefas
def todas_tarefas():
    '''Abre o arquivo com as tarefas e mostra ao usuario'''
    with open('list_tarefas.txt', 'r') as listat:
        total = listat.read()
        print('\nEssas são suas tarefas:')
        print(total)
        print('Já finalizou alguma hoje? Vamos dar o nosso melhor! 😄')

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
            adicionar_tarefas()  # Agora chama a função
        elif opcao == "2":
            todas_tarefas()  # Agora chama a função
        elif opcao == "3":
            print("Função de marcar tarefa aqui.")  # Pode implementar depois
        elif opcao == "4":
            print("Função de excluir tarefa aqui.")  # Pode implementar depois
        elif opcao == "5":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()