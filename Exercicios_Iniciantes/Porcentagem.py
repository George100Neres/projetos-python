# Faça um algoritmo que leia o preço de um produto e mostre 
# seu novo preco com 5% deconto.

preco = float(input('Qual e o preco do produto? RS'))
novo = preco - (preco * 5 / 100)
print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar {.2f}'.format(preco, novo))


