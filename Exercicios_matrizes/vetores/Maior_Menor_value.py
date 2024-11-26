# Faça um programa que leia 5 valores numericos e gaurde-os em uma lista. No final, mostra qual foi o maior e o 
# menor valor digitado e as susa respectivas posições na lista.

listanum = []
mai = 0
men = 0
for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor pra posicao {c}:')))
    if c == 0:
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]

print('=-' * 30)
print(f'Você digitou os valores {listanum}')
print(f'O maior valor digitado foi {mai} nas pocições ', end='')

for i, v in enumarate(listanum):
    if v == mai:
        print(f'{i}---', end='')
print(f'O menor valor digitado foi {men} nas posicoes ', end='')

