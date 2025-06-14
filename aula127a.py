import json

CAMINHO_ARQUIVO = 'aula127.json'

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


p1 = Pessoa("Dom Ruam", 33)
p2 = Pessoa("Helena Pavosky", 21)
p3 = Pessoa("Joelma Patino", 22)

db = [vars(p1), vars(p2), vars(p3)]

def realizar_dump():
    with open(CAMINHO_ARQUIVO , 'w') as arquivo:
        json.dump(db, arquivo, ensure_ascii=False, indent=2)
        print('401 - Ok ---> Dump Realizado Com Sucesso!!!')
