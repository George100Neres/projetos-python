# Crie uma função de um parametro. Essa função retorna o valor da string 'P',
# se seu argumento for positivo, e 'N', seu seu argumento for zero ou negativo.

def valor(x):

    x = int(input("Digite algum valor"))
    if x > 0:
        print('P')
    else:
        print('N')

    print(valor(10))
