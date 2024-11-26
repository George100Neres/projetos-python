
# Faça um programa que que atenda os seguintes requisitos:

# A soma de todos os valores pares digitados
#A soma dos valores da terceira coluna, 
#C O maior valor da segunda inha.


matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = mai = scol = 0

for l in range(0, 3):
  for c in range(0, 3):
    matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
    print('-----' * 20)
    for l in range(0, 3):
       for c in range(0, 3):
         print(f'[{matriz [l] [c]: }]', end='')
       if matriz[l] [c] % 2 == 0:
         spar += matriz [l] [c]
    print('==' * 30)

    print(f'A soma dos valroes pares é {spar}')   

    # Logica para ler a somatoria da 2 linha
    for l in range(0, 3):
        scol += matriz[l] [2]
        print(f'A soma dos valores da terceira coluna e {scol}' )

    for c in range(0, 3):
       if c == 0:
          mai = matriz[l] [c]
       elif matriz[l] [c] > mai:
          mai = matriz[l] [c]
    print(f'O maior valr da segunda linha é {mai}.')

