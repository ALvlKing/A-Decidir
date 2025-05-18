#1. Adiconar Tarefa
def adicionar_tarefas():
    '''Abre o arquivo da lista de tarefas e escreve as atividades do usario em um documento txt'''
    with open('list_terefas.txt', 'a') as listat:
        tarefa = input('Digite sua Tarefa:\n')
        listat.write = (tarefa + '/n')

    '''Abre o arquivo no modo de leitura para que o usuario veja se o que o mesmo escreveu foi salvo corretamente'''
    with open('list_terefas.txt', 'r') as listat:
        conteudo = listat.read()
        print('/nSuas tarefas:')
        print(conteudo)

#----------------------------------------------------------------------------------------------------------------------
#2. Ver Tarefas
def todas_tarefas():
    '''Abre o arquivo com as tarefas e mostra ao usuario'''
    with open('list_terefas.txt', 'r') as listat:
        total = listat.read()
        print('/nEssas são suas tarefas:')
        print(total)
        print('Já finalizou alguma hoje? Vamos dar o nosso melhor! 😄')

