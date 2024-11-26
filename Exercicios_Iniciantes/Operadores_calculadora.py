# Crie um programa que leai dois valores e mostre um menu como o
# ao lado na tela:
#Seu programa devera realizar a operação solicitada em cada caso.

n1 = int(input('Primeiro valor'))
n2 = int(input('Segundo valor'))
opcao = 0
while opcao != 5:

 print('''[ 1 ] somar
         [ 2 ]multiplicar
         [ 3 ]maior
         [ 4 ]novos numeros
         [ 5 ]sair do programa
         Qual e a sua opção?''')

opcao = int(input(' >>>>>>>Qual é a sua opção? '))
if opcao == 1:
   soma = n1 + n2
   print('A soma entre {} e {}'.format(n1, n2, soma))
elif opcao == 2:
    produto = n1 * n2
    print('O resultado de {} x {} é {}'.format(n1, n2, produto))
elif opcao == 3:
     if n1 > n2:
        maior = n1
     else:
        maior = n2
elif opcao == 4:
    print('Infome os numeros novamente')
    n1 = int(input('Primeiro valor: '))
    n2 = int(input('Segundo valor: '))
elif opcao == 5:
      print('Saiu do programa')
else:
    print('Opcao invalida. Tente novamente')
    print('=-=' * 10)
    
print('Fim do programa! Volte sempre')

