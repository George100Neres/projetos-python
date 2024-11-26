"""
Repetições 
while (enquanto)
Executa a condição enquanto for verdadeira
"""

condicao = True

while condicao:
    nome = input('Qual o seu nome?: ')
    print('Seu nome é {nome}')

    if nome == 'sair':
        break

print('Acabou')


