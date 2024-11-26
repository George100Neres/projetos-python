# Faça um programa que pegue um numero do teclado e calcule a soma de 
#todos os numeros EX: Usuario digita 7, programa mostra 28, pois 1+2+3+4+5+6+7 = 28

numero = int(input("Digite um numero"))

som = 0
for i in range(1, numero+1):
    print(int(i))
    som = som + i

print (som)