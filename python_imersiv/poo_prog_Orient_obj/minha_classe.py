"""
class - Classes são moldes para criar novos objetos
As classes geram novos obetos (instâncias) que podem
ter seus próprios atributos e métodos. Os objetos gerados
pela classe podem usar seus dados internos para realizar varais ações.
Por convenção, usamos PascalCase para nomes de classes.
string = 'Luiz' #str
"""
class ControleRemoto:
 # Atributos do Controle Remoto
    def __init__(self, televisao, comodo):
        self.televisao = televisao
        self.comodo = comodo
  # FUnções do COntrole Remoto
    def avancar_canal(self):
        print('Canal Avançado')

    def voltar_canal(self):
        print('Voltar o canal')

    def escolher_canal(self, canal):
        print('Alterado para o canal: {}'.format(canal))


controle_sala = ControleRemoto('samsung', 'sala')
print(controle_sala.comodo)
print(controle_sala.televisao)
controle_sala.avancar_canal()
controle_sala.escolher_canal(12)

controle_sala = ControleRemoto('samsung', 'sala')