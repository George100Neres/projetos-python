# Faça um programa que conte de 10 a 25, mosntrando na tela cada numero somando com o anterior.


i = 10
while i <= 25:
    if i == 10:
        print str(i)
    else:
        ant = i - 1
        print str(i) + " " + str(i + ant)
        i = i + 1

