
x, y, *resto = 1, 2, 3, 4
print(x, y, resto)

def soma(*args):
    total = 0
    for numero in args:
        print('Total', total, numero)
        total = total + numero
        print('Total', total)

soma(1, 2, 3, 4, 5, 6)

# Resultado da somatoria dos numeros R = 6

soma_1_2_3 = soma(1, 2, 3)
print(soma_1_2_3)

# Resultado da somatoria dos numeros R = 15
soma_4_5_6 = soma(4, 5, 6)
print(soma_4_5_6)

# Função Somatoria
print(sum(1, 2, 3, 4, 5, 6, 7, 78, 10))
