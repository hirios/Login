from flask import Flask
from pprint import pprint
import socket


def ip():
    # Obtendo o ip do pc na rede

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]


def page():
    # Abre o txt com os usuários e separa user por user e coloca numa lista
    users = open("users.txt", "r")
    user_list = users.read().split()

    # Um laço que cria uma html com cada usuário dentro da lista web
    web_page = []
    for user in user_list:
        web_page.append(f'<h1>|{user}| <a SIZE="20" </a> </h1>\n')

    # Cria uma string a partir da minha lista web_page, para que seja renderizada
    web_page = "".join(web_page)
    return web_page


app = Flask(__name__)

#especificando caminho a partir da url (asdasd:000/teste)
@app.route("/")
def hello():
    return page()

# host especificando o ip do meu computador/ refresh a cada alteração na página
app.run(host=ip(), use_reloader=True)
























## Calcular combinações possívels sem repetição e tendo ordem como sem importância
##import itertools
##
##my_list = [1,2,3,4,5]
##all_combs = []
##for n in range(1, len(my_list) + 1):
##    all_combs.extend(itertools.combinations(my_list, n))
##
##for item in range(0, len(all_combs)):
##    print(all_combs[item])
##
##print(len(all_combs))
