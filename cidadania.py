class Pessoa():
    nome = None
    sexo = None
    idade = None

    def __init__(self, nome, sexo, idade):
        self.nome = nome
        self.sexo = sexo
        self.idade = idade

class Cidadao(Pessoa):
    cpf = None

    def __init__(self, nome, sexo, idade, cpf):
        super().__init__(nome,sexo,idade)
        self.cpf = cpf

nome = input("Nome da pessoa: ")
sexo = input("Sexo da pessoa: ")
idade = input("Idade da pessoa: ")
cpf = input("Cpf da pessoa: ")

cidadao_1 = Cidadao(nome,sexo,idade,cpf)

print(f"Nome: {cidadao_1.nome}")
print(f"Sexo: {cidadao_1.sexo}")
print(f"Idade: {cidadao_1.idade}")
print(f"CPF: {cidadao_1.cpf}")
