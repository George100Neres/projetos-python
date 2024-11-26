
# Classe Pai
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def fazer_som(self):
        pass

    def imprimirNome(self):
        print(f'O nome do animal é: ', self.nome)

# Classes Filhos
class Cachorro(Animal):
    def fazer_som(self):
        return "Miauu!"


class Gato(Animal):
    def fazer_som(self):
        return "Miauu!"

class Passarinho(Animal):
    def fazer_som(self):
        return "Piu piu!"



# -----------------------

# Criação dos animais

cachorro = Cachorro("Bilu")
gato = Gato("Fofuxo")
passarinho = Passarinho("Pintinho Amarelinhio")

# Imprime os sons dos bichos

print(cachorro.nome + " faz: " + cachorro.fazer_som())
print(gato.nome + " faz: " + gato.fazer_som())
print(passarinho.nome + " faz: " + passarinho.fazer_som())

cachorro.imprimirNome()
gato.imprimirNome()
passarinho.imprimirNome()

#Polimorfismo

def fazer_barulho(animal):
    print(animal.nome + " faz: " + animal.fazer_som())

    cachorro = Cachorro("Bilu")
    gato = Gato("Fofuxo")
    #Animal que ira fazer Barulho
    fazer_barulho(passarinho)

