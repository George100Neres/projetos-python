# Um professor passa quantas notas ele quiser
# Quer a media de todas as notas
# MEdia for menor que 6 => O aluno sera reporvado
# Caso contrario => O aluno está aprovado

notas =[]
while(True):
    nota = float(input("Insira a proxima nota. "))
    notas.append(nota)
    resposta = input("Quer inserir mais uma nota? (s/n)")
    if (resposta == 'n'):
        break

    soma = 0


for valor in notas:
    soma += valor

media = soma / len(notas)
print(f'Media = {media}')

if (media < 0):
    print("Reprovado")
else:
    print("Aprovado")
