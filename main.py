def adicionar_tarefas():
    '''Abre o arquivo da lista de tarefas e escreve as atividades do usuário em um documento txt'''
    with open('list_terefas.txt', 'a') as listat: 
        tarefa = input('Digite sua Tarefa:\n')
        # Correção: write() é função e não precisava do "=", '\n' faz a quebra de linha.
        listat.write(tarefa + '\n')

def todas_tarefas():
    '''Abre o arquivo com as tarefas e mostra ao usuário'''
    with open('list_terefas.txt', 'r') as listat:
        total = listat.read()
        # Correção: '\n' é a quebra de linha.
        print('\nEssas são suas tarefas:')
        print(total)
        print('Já finalizou alguma hoje? Vamos dar o nosso melhor!')

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

# O menu deixamos por último.
menu()
