import requests
import fire
from charada import *


def listuser(url="http://192.168.0.104:5000/", separador="|"):
    global users

    # Requisitando minha página com a lista de usuários
    # Dei um split pra separar usuário por "|"
    # Depois faço um laço listando cada um deles e adiciono a LISTA users

    try:
        var = requests.get(url, timeout=40)
    except:
        print('Falha ao realizar conexão')

    var = (var.text).split(separador)
    users = []

    for c in range(1, len(var), 2):
        users.append(var[c])


def checkuser(username='Python'):
    # se username estiver dentro da lista "users" retorna cad/inex:

    username = codificar(username)
    if username in users:
        return 'cadastrado'
    else:
        return 'inexistente'


if __name__ == "__main__":
    listuser()
    fire.Fire(checkuser)
