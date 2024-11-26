"""
Escopo de funções em Python
Escopo significa o local onde aquele codigo pode atingir
Existe o escopo global e local
O escopo global e o escopo onde todo o codigo é alcaçavel
O escopo local e o escopo onde apenas nomes do mesmo local
podem ser alcançados
Não temos acesso a nomes de escopos internos nos escopos externos.
A palavra global faz uma variavel dop escopo externo ser a 
mesma no escopo itnerno.
"""

x = 1

def escopo():
    #global x
    x = 10

def outra_funcao():
    #global x
    x = 11
    y = 2
    print(x, y)

# imprime o 11 e 2
outra_funcao()

#print(x)
escopo()
