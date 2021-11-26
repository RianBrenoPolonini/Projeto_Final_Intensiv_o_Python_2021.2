import pickle
from pprint import pprint


def listar_users(tipo=0, genero='', ordenar=0):
    try:
        arq = open('users.txt', 'rb')
    except:
        return False, 'Arquivo com usuarios não exite.'

    users = pickle.load(arq)
    arq.close()

    if not users:
        return False, 'Nenhum identificado.'
    elif not tipo and not genero and not ordenar:
        return True, users

    users_filtrado = []

    if tipo:
        users_filtrado = [user for user in users if user['tipo'] == tipo]

    if genero:
        if not users_filtrado:
            users_filtrado = [
                user for user in users if user['genero'] == genero.upper()
            ]
        else:
            users_filtrado = [
                user for user in users_filtrado if user['genero'] == genero
            ]

    if ordenar:
        if not tipo and not genero:
            if ordenar == 1:
                users_filtrado = sorted(users, key=lambda k: k['nome'])
            else:
                users_filtrado = sorted(users, key=lambda k: k['data_nascimento'])
        else:
            if ordenar == 1:
                users_filtrado = sorted(users_filtrado, key=lambda k: k['nome'])
            else:
                users_filtrado = sorted(users_filtrado, key=lambda k: k['data_nascimento'])

    if not users_filtrado:
        return False, 'Nenhum identificado.'
    return True, users_filtrado


def buscar_por_matricula(matricula):
    if not matricula:
        return False, 'Informe a matricula para fazer a busca'

    users = listar_users()
    users_filtrado = []

    if users[0]:
        try:
            for i in matricula:
                for user in users[1]:
                    if user['matricula'] == i:
                        users_filtrado.append(user)
        except:
            users_filtrado = [
                user for user in users[1] if user['matricula'] == matricula
            ]

    if not users_filtrado:
        return False, 'Nenhum identificado.'
    return True, users_filtrado


def busca_users(string):
    if not string or len(string) < 3:
        return False, 'Digite pelo menos 3 letras para fazer a busca.'

    users = listar_users()
    users_filtrado = []

    if users[0]:
        users_filtrado = [
            user for user in users[1]
            if string.lower() in user['nome'].lower()
        ]

    if not users_filtrado:
        return False, 'Nenhum identificado.'
    return True, users_filtrado


def aniversariantes_mes(mes):
    if not mes:
        return False, 'Digite o mês para fazer a busca.'

    users = listar_users()
    users_filtrado = []

    if users[0]:
        users_filtrado = [
            user for user in users[1]
            if mes == int(user['data_nascimento'][3:5])
        ]

    if not users_filtrado:
        return False, 'Nenhum identificado.'
    return True, users_filtrado


def listar_disciplinas(extrapolam=False):
    try:
        arq = open('disciplinas.txt', 'rb')
    except:
        return False, 'Arquivo com disciplinas não exite.'

    disciplinas = pickle.load(arq)
    arq.close()

    if not disciplinas:
        return False, 'Nenhuma identificada.'
    elif not extrapolam:
        return True, disciplinas

    disciplinas_filtrado = [disciplina for disciplina in disciplinas if len(disciplina['alunos']) >= 40]

    for disciplina in disciplinas_filtrado:
        disciplina['professor'] = buscar_por_matricula(disciplina['professor'])[1]

    if not disciplinas_filtrado:
        return False, 'Nenhuma identificada.'
    return True, disciplinas_filtrado


def buscar_disciplina(codigo):
    if not codigo:
        return False, 'Informe o código para fazer a busca'

    disciplinas = listar_disciplinas()
    disciplina = []

    if disciplinas[0]:
        disciplina = [disciplina for disciplina in disciplinas[1] if disciplina['codigo'] == codigo]
        if not disciplina[0]['alunos']:
            disciplina[0]['alunos'] = 'Sem alunos cadastrados ainda'
        else:
            disciplina[0]['alunos'] = buscar_por_matricula(disciplina[0]['alunos'])[1]

    if not disciplina:
        return False, 'Nenhum identificado.'
    return True, disciplina

def matriculado_menos_de_tres():
    alunos = listar_users(1)
    disciplinas = listar_disciplinas()

    if not alunos[0]:
        return False, 'Sem alunos cadastrados'
    
    if not disciplinas[0]:
        return False, 'Sem disciplinas cadastradas'

    alunos_filtrados = []

    for aluno in alunos[1]:
        contador = 0
        for disciplina in disciplinas[1]:
            if aluno['matricula'] in disciplina['alunos']: 
                contador += 1
        
        if contador < 3:
            alunos_filtrados.append(aluno)

    if not alunos_filtrados:
        return False, 'Nenhuma identificada.'
    return True, alunos_filtrados
