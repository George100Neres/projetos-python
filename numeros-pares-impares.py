"""
 Faça um programa que prça ao usuário para digitar um numero inteiro, informe
 se este número é par u ímpar. Caso o usuario nao digite um número inteiro,
 informe que não é um numero inteiro.
"""

entrada = input('Digite um número')

if entrada.isdigit():
    entrada_int = int(entrada)
    par_impar = entrada_int % 2 == 0
    par_impar_texto = 'impar'

    if par_impar:
        par_impar_texto = 'par'

    print(f'O número {entrada_int} é {par_impar_texto}')
else:
    print('VocÊ não digitou um número inteiro')


