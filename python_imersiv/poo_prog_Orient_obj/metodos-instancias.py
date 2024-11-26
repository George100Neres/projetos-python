# MEtodos em instancias de classes Python
# Hard coded - È algo que foi escrito diretaente no código

class Carro:
    def __init__(self, nome):
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} está acelerando...')

# Imprime todos os caracteres maiusculos
string = 'Luiz'
print(string.upper())

fusca = Carro('Fusca')
print(fusca.nome)
fusca.acelerar()

