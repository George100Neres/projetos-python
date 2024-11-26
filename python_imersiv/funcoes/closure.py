"""
Closure e funções que retornam outras funções
"""

def criar_saudacao(saudacao, nome):
    return f'{saudacao}, {nome}!'


s1 = criar_saudacao('Bom dia', 'Luiz')
s2 = criar_saudacao('Boa noite', 'Luiz')
print(s2)