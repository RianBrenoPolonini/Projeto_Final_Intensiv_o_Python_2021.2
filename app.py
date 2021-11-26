from pprint import pprint

from users import users_cadastro
from disciplinas import disciplinas_cadastro
import relatorios as relatorios


menu = input("""
Digite o número correspondente ao que deseja fazer:

    (1) - Cadastrar Aluno/Professor
    (2) - Cadastrar Disciplina
    (3) - Relatório
""")

if menu == '1':
    dados = {
        "nome":
        input("Nome: "),
        "genero":
        input("Gênero (M para masculino, F para feminino): "),
        "data_nascimento":
        input("Digite o dia de nascimento: ") + "/" +
        input("Digite o mês de nascimento (Só números): ") + "/" +
        input("Digite o ano de nascimento: "),
        "cpf":
        input("Digite o CPF: "),
        "tipo":
        input("Digite 1 se for Aluno(a) ou 2 se for professor(a): ")
    }
    cadastro = users_cadastro(dados)

    if cadastro[0]:
        print("Usuário cadastrado com sucesso!\n")
        pprint(cadastro[1])
    else:
        print(cadastro[1])

elif menu == '2':
    dados = {
        "nome":
        input("Nome: "),
        "codigo":
        input("Código: "),
        "semestre":
        input("Semestre: "),
        "professor":
        input("Digite a matricula do professor: "),
        "alunos": list(map(int,input("Digite as matriculas dos alunos separados por espaço: ").split()))
    }

    cadastro = disciplinas_cadastro(dados)

    if cadastro[0]:
        print("Disciplina cadastrado com sucesso!\n")
        pprint(cadastro[1])
    else:
        print(cadastro[1])

elif menu == '3':
    menu = input("""
Digite o número correspondente ao que deseja fazer:

    (1) - Listar todos os Alunos e Professores
    (2) - Listar só Alunos
    (3) - Listar só Professores
""")

if menu == '1':
    pprint(relatorios.listar_users()[1])
elif menu == '2':
    pprint(relatorios.listar_users(1)[1])
elif menu == '3':
    pprint(relatorios.listar_users(2)[1])