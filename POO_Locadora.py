class Filme:
    def __init__(self, titulo, disponivel):
        self.titulo = titulo
        self.disponivel = disponivel
    def alugar(self):
        self.disponivel = False
    def devolver(self):
        self.disponivel = True

class Cliente:
    def __init__(self, nome):
        self.nome = nome

class Aluguel:
    def __init__(self, filme, cliente):
        self.filme = filme
        self.cliente = cliente
        self.filme.alugar()

Filme1 = Filme("A volta dos que não foram", False)
Cliente1 = Cliente("Pedro")
Aluguel1 = Aluguel(Filme1, Cliente1)

Filme1.alugar()

print(f"Filme: {Filme1.titulo}, Disponível: {Filme1.disponivel}")
print(f"Cliente: {Cliente1.nome}")
print(f"Aluguel: Filme '{Aluguel1.filme.titulo}' alugado por {Aluguel1.cliente.nome}")

Filme1.devolver()

print(f"Filme: {Filme1.titulo}, Disponível: {Filme1.disponivel}")