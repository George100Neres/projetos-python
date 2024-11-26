
"""
 Faça um programa que pergunte a hoa ao usuário e, baseando-se no horário
 descrito, exiba a saudação apropriada. Ex.
 Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
 """

hora = input('Que horas?')
usuario = int(hora)

if usuario <= 11:
    print('Bom Dia')
elif usuario >=12 and  usuario<=17:
    print('Boa tade')
else:
    print('Boa noite')

