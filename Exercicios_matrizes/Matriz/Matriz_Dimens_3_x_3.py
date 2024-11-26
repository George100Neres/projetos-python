# Crie um programa que crie uma amtriz de dimensão 3 x 3 e preencha 
# com valores lidos pelos teclados.

# No final, mostre a matriz na tela, com a formatação correta.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(0, 3):
  for c in range(0, 3):
    matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
    print('-----' * 20)

for l in range(0, 3):
   for c in range(0, 3):
     print(f'[{matriz[l] [c]}]', end='')
