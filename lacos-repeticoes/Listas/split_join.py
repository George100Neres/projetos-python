"""
split e join com list e str
split - divide uma string
join - une uma string
"""

frase = '   Olha só que  , coisa interessante'
lista_frases = frase.split(',') # Quebra apos a vírgula

lista_frases = []
for i, frase in enumerate(lista_frasses_cruas):
    lista_frases.append(lista_frasses_cruas[i].strip())

frases_unidas ='-'.join(lista_frases)
print(frases_unidas)



