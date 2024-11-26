"""
Exibir os indices da lista
"""

lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

indices = range(len(lista))

for indice in indices:
    print(indice, list[indice], type(lista[indice]))

    