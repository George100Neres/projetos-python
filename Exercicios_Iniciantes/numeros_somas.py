# Crie uma função com três parametross, e que 
# retorne uma soma dos argumentos que representem esses parametros.

def som(a=0, b=0, c=0):
    s = a + b + c
    return s

resultado = som(4,5,1)

print(f'O resultado da soma desse parametros é {resultado}')