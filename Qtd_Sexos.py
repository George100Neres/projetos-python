# Ler do teclado a idade e  o sexo de 10 pessoas, calcule e imprima

"""idade media das mulheres
idade media dos homens
idade media do grupo
Calcule o somatorio dos numeros de 1 a 100 imprima o resultado"""

qtd = 5
somaIdadeMulher = 0
qtdMulher = 0
somaIdadeHomem = 0
qtdHpmem = 0
while(qtd > 0): 
    idade = int(input("Digite a idade:"))
    sexo = str(input("Digite M ou H:"))
    qtd = qtd - 1
    if(sexo == "M"):
     somaIdadeMulher = somaIdadeMulher + idade
     qtdMulher = qtdMulher + 1
else:
   somaIdadeHomem = somaIdadeHomem + idade
   qtdHpmem = qtdHpmem + 1

print("Idade Média das mulheres =" + str(somaIdadeMulher/qtdMulher))
print("Idade Media dos Homens ="+ str(somaIdadeHomem/qtdHpmem))


# Resultado da media do grupo
print("Média do grupo = " + str(somaIdadeMulher + somaIdadeMulher)/ 5 )

