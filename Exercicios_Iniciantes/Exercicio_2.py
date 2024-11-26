# Faça um programa que mostre na tela todos os numeros de 1 a 100 usandos laços pelo usuario.
#Para cada leitura, multiplique o numero lido por tres e imprima a multicação no terminal.
#Caso o numero multipliqcado seja maior que 100, o programa deve encerrar.

numero = int(input("Informe um NUmero que seja menor que 100 "))

while numero < 100:
    numero  = (numero + 1) * 32
    print(numero)


print('Acabou')