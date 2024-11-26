"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
"""


#        +01234
#        -54321
string = 'ABCDE'
lista = [123, True, 'George Neres', 1.2 []]

print(lista)

#        0    1      2              3    4
#       -5   -4     -3             -2   -1
lista = [123, True, 'Luiz Otávio',  1.2, []]
lista[-3] = 'Maria' # Vai alterar o valor do indice
print(lista)
print(lista[2], type(lista[2]))
