#1. Adicionar Tarefas
def adicionar_tarefas():
'''Abre o arquivo da lista de tarefas e escreve as atividades do usario em um documento txt'''
    with open('list_terefas.txt', 'a') as listat:
        tarefa = input('Digite sua Tarefa:\n')
        listat.write = (tarefa + '/n')
#----------------------------------------------------------------------------------------------------------------
'''Abre o arquivo no modo de leitura para que o usuario veja se o que o mesmo escreveu foi salvo corretamente'''
    with open('list_terefas.txt', 'r') as listat:
        conteudo = listat.read()
        print('/nSuas tarefas:')
        print(conteudo)
