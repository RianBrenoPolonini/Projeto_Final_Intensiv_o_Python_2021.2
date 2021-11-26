import pickle
from pprint import pprint

def users_cadastro(dados = {}):
    
    # dados = {
    #     "nome": "Rian",
    #     "genero": "M/F",
    #     "data_nascimento": "17/02/2005",
    #     "cpf": "12345678911",
    #     "tipo": 1/2 
    #     # 1 = aluno/ 2 = professor
    # }

    if not dados or not dados["nome"] or not dados["genero"] or not dados["data_nascimento"] or not dados["cpf"] or not dados["tipo"]:
        return False, "Digite todos as informações para fazer cadastro."

    if len(dados["cpf"]) != 11:
        return False, "Digite um CPF valido."

    if dados["tipo"] not in ("1","2"):
        return False, "Digite se é Aluno(a) ou Professor(a)."

    dados["nome"] = dados["nome"].lower()
    dados["genero"] = dados["genero"].upper()
    dados["tipo"] = int(dados["tipo"])

    if dados["genero"] not in ("M", "F"):
        return False, "Digite M para gênero masculino ou F para feminino."

    try:
        arq = open("users.txt", "rb")
        users = pickle.load(arq)
        arq.close()

        for user in users:
            if user["cpf"] == dados["cpf"]:
                return False, "CPF já cadastrado!"

        dados["matricula"] = users[-1]["matricula"] + 1

        users.append(dados)

        arq = open("users.txt", "wb")
        pickle.dump(users, arq)
        arq.close()

        return True, dados

    except:
        user = []
        dados["matricula"] = 2100001
        user.append(dados)

        arq = open("users.txt", "wb")
        pickle.dump(user, arq)
        arq.close()

        return True, dados

