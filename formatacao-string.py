
"""
Formatação básica de strings 
s  - string
d  - int
f  - float
< numero de dígitos> f
x ou X - Hexadecimal
(Caractere) (><^) (quantidade)
> - Esquerda
< - Direita
^ - Centro
Sinal  -  +  ou  -
Ex.: 0>- 100, .1f
Conversion flags  -  Ir ls !a

"""
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'{variavel: <10}.')
print(f'{1000.45672151298232:0=+10,.1f}')
print(f'O hexadecimal de 1500 é {1500:08X}')



