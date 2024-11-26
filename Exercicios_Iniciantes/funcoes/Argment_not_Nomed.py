"""
args - argumentos nao nomeados
*  -  * (empacotamento e desempacotamento)
"""

#Lembre do desempacotamento

x, y, *resto = 6, 5, 4,3

print(x, y, resto)


def num(*args):
    print(args, type(args))

    num(1, 2, 3, 4, 5, 6, 7)