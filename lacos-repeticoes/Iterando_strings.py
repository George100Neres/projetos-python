"""
Iterando strings com while
"""

#       01234567890
# nome = 'Luiz Otávio'  # Iteraáveis
nome = 'Luiz Otávio' # Iteraceis

indice = 0
novo_nome = '' # Nao tem nada na variavel
# Leitura do While
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

    novo_nome += '*'
    print(novo_nome)
