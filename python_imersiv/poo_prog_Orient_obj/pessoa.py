class Pessoa:

    # Atributos CFPF
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        # Atributo privado
        self.__cpf = cpf

#Metodos publicos
    def correr(self):
        print('Estou correndo')

    def beber(self, bebida):
        if bebida == 'cerveja':
            self.__apresentar_documento()
        print('bebendo...')
# Meetodo Privado
    def __apresentar_documento(self):
        print(self.__cpf)

ronaldo = Pessoa('Ronaldo', 32, '654123987')
print(ronaldo.nome)
print(ronaldo.idade)
ronaldo.__apresentar_documento()




