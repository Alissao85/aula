class Carro:
    def __init__(self, nome):
        self.nome = nome

    def acelerar(self):
        print(f'O {self.nome} esta acelerando')

    def freiar(self):
        print(f'O {self.nome} esta freiando')
        

fusca = Carro('fusca')
Carro.acelerar(fusca)

celta = Carro('celta')
Carro.freiar(celta)

print(fusca.nome)
print(celta.nome)
