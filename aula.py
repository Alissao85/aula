# textos = 'Alissão'
# print(textos.lower())
# print(isinstance(textos, str))

# class Pessoa:
#     ...
# p1 = Pessoa()
# p1.nome = 'Alissão'
# p1.sobrenome = 'Vital'
# print(p1.nome)
# print(p1.sobrenome)
# print()
# p2 = Pessoa()
# p2.nome = 'Marcia'
# p2.sobrenome = 'Porto'
# print(p2.nome)
# print(p2.sobrenome)
# print()
# p3 = Pessoa()
# p3.nome = 'Eginal'
# p3.sobrenome = 'Vital'
# print(p3.nome)
# print(p3.sobrenome)

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

p1 = Pessoa('Alissão', 'Vital')
# p1.nome = 'Alissão'
# p1.sobrenome = 'Vital'
print(p1.nome)
print(p1.sobrenome)
print()
p2 = Pessoa('Marcia', 'Porto')
# p2.nome = 'Marcia'
# p2.sobrenome = 'Porto'
print(p2.nome)
print(p2.sobrenome)
print()
p3 = Pessoa('Egina', 'Vital')
# p3.nome = 'Eginal'
# p3.sobrenome = 'Vital'
print(p3.nome)
print(p3.sobrenome)