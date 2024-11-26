# Crie um programa que faça o computador jogar jojenpô com você

from random import randint
itens = ('Pdra', 'Papel', 'Tesoura')
computador = randint(0,2) # compuador vai jogar entre 0 e 2
print('O computador escolheu {}'.format(computador))
print('''Suas opções:
[ 0 ]  PEDRA
[  1 ]       
[  2 ] '''  )
jogador = int(input('Qual e a sua jogada?  '))
print('-=' * 11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 11)
