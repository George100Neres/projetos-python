# Faça um programa que peça 2 números inteiros e um numero real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo
#a soma do triplo com oterceiro
# o terceiro elevado ao cubo

num_1 = int(input('Digite um numero inteiro -->'))
num_2 = int(input('Digite um numero inteiro -->'))
num_3 = int(input('Digite um numero inteiro -->'))

resultado_1 = (num_1 * 2) * (num_2 / 2)
resultado_2 = (num_1 * 3) + num_3
resultado_3 = num_3 ** 3

print('O produto do dobro do priemiro com a metade do segundo é {resultado_1}')
print(f'A soma do triplo do primeiro com o terceiro é {resultado_2}')
print(f'O terceiro elevado ao cubo é {resultado_3:.2f}')

