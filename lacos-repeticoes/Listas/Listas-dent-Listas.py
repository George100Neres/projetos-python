"""
Lista de listas e seus índices
"""
salas = [
    # 0        1
    ['Maria', 'Helena', ],  # 0
    # 0
    ['Elaine', ],  # 1
    # 0       1       2
    ['Luiz', 'João', 'Eduarda', (0, 10, 20, 30, 40)],  # 2
]
  
  # Busquei a Helena

print(salas[1][0]) # Busquou a Elaine 
print(salas[0][1])  # Busquou a Helena
print(salas[2][2]) # Busquou a Eduarda
print(salas[2])
print(salas[2][3][3])

for sala in salas: 
    print(f'A sala é {sala}')
    for item in sala:
        print(aluno)

