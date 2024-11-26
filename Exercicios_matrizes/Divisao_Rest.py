# Faca um programa que realize a a soma dos 3 digitos, e exiba na tela o resultado da divisao e o resto

num1 = int(input("Infome o primero numero"))
num2 = int(input("Infome o segundo numero"))
num3 = int(input("Infome o terceiro numero"))

result_div = (num1 + num2 + num3) / 3
rest_div = result_div % 1

print("O resultado da  divisao", {result_div})
print("O resto da  divisao", {rest_div})