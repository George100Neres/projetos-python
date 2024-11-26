"""

Iterado strings com while
"""
#       012345678910
nome = 'Maria Helena' #Iteráveis
#       111985321475

indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

novo_nome += '*'
print(novo_nome)

