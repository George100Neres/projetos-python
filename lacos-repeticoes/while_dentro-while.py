"""
Repeticoes
while(enquanto)
Executa uma ação enquanto uma condiucao for verdadeira
Loop infinito -> Quando um codigo nao tem fim
"""

qtd_linhas = 5
qtd_colunas = 5

linha = 1

while linha <= qtd_linhas:
    # Cria-se uma variavel apos entrar no while
    coluna = 1
    while coluna <= qtd_colunas:
        print(f'{linha=} {coluna=}')
        coluna += 1
        linha +=1

    print('Acabou')



