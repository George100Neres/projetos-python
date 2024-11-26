
#ler 3 notas obter a media e aprovado ou não > 7.0

notas = []

#for 
# Qtd maxima de notas
for i in range(3):
    nota = float(input("Digite a nota "+ i + ":"))
    notas.append(nota) # 

media = sum(notas) / len(notas)

if media >= 7.0:
    print("O aluno foi aprovado:")
else:
    print("O aluno foi reprovado")
print("Média", media)




             