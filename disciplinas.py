import pickle
from pprint import pprint


def disciplinas_cadastro(dados={}):

    # dados = {
    #     "nome": "Prog I",
    #     "codigo": "2515",
    #     "semestre": "2021.2",
    #     "professor": "2100001"
    #     "alunos" : [2100002,2100003]
    # }

    if not dados or not dados["nome"] or not dados["codigo"] or not dados[
            "semestre"] or not dados["professor"]:
        return False, "Digite todas as informações para fazer cadastro."

    try:
        arq = open("disciplinas.txt", "rb")
        disciplinas = pickle.load(arq)
        arq.close()

        disciplinas.append(dados)

        arq = open("disciplinas.txt", "wb")
        pickle.dump(disciplinas, arq)
        arq.close()

        return True, dados

    except:
        disciplinas = []
        disciplinas.append(dados)

        arq = open("disciplinas.txt", "wb")
        pickle.dump(disciplinas, arq)
        arq.close()

        return True, dados
