# __dict__ vars para atributos de instância
class Pessoa:
    ano_atual = 2025

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def getAnoNascimento(self):
        return Pessoa.ano_atual - self.idade


p1 = Pessoa('Romêu', 25)
p2 = Pessoa('Julieta', 24)

print(Pessoa.ano_atual)

print(p1.getAnoNascimento())
print(p2.getAnoNascimento())
print(p1.__dict__)
print(vars(p1))