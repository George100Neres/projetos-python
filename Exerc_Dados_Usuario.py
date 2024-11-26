
"""
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade foram digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu noome contem (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome étry-catch.py
          {letra}
        A ultima letra do seu nome é {letra}
Se nada for digitado em nome ou idade:
    exiba "Desculpe, você deixou campos vazios."
   """

nome = input('DIgite o seu nome: ')
idade = input('Digite sua idade: ')

if  nome and idade:
    print(f'Seu nome e {nome}')
    print(f'Seu nome invertido e {nome[::-1]}')

if ' ' in nome:
    print('Seu nome contém espaços')

else:
    print('Seu nome NÂO contem espaços')

    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do sue nome é {nome}')
else:
    print("Desculpe, você deixou campos vazios.")