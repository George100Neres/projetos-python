"""
Cuidados com dados mútaveis
- copiado o valor (imutávies)
aponta para o mesmo valor na memoria
"""

lista_a = ['Luiz', 'Maria', 1, True, 1.2]
lista_b = lista_a.copy()

lista_a[0] = 'Qualquer coisa' # Substitui o valor do Indice
print(lista_a)
print(lista_b)