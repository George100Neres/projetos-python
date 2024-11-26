
num_alunos = 2
nomes = []
notas = []
media = 0

for i in range (num_alunos): 
    nomes.append(input(f'Informe o noem do aluno {i+1}: '))
    notas.append(float(input(f'Infome a nota de {nomes[i]}: ')))
    media = media + notas[i]

media = media / num_alunos
print(f'A média da turma é {media:.2f}.')

for i in range (num_alunos):
    if notas[i] > media:
        print(f'Parabéns {nomes[i]}')