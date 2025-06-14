class Animal:
    def __init__(self, nome):
        self.nome = nome

        data = "14/06/2025"
        print(data,'\n')

    def comer(self, alimento):
        self.alimento = alimento
        return f'O {self.nome} está comendo {alimento}'

leao = Animal('Leão')
print(leao.nome, '\n')
print(leao.comer('Uva'), '\n')