"""
Valores padrao para parametros Ao definir uma função, os parametros 
podem ter valores padrao. Caso o valor nao seja enviado para o parametro
o valor padrao será usado.

"""

def soma(x, y, z=0):

    print(f'{x=} {y=} {z=}', x + y + z)

soma(1, 3)
soma(4, 6)
