"""
Escopo significa o local onde aquele codigo pode atingir
* Exite escopo local e global
* O escopo global e o escopo onde todo o codigo e alcançavel
* O escopo local e o escopo onde apenas nomes do msm local podem ser alcançados.
* Nao temos aceesso a nomes de escopos internos nos escopos externos.
* A palavra global faz uma variavel do escopo externo 
ser a mesma no escopo interno.
"""

x = 1

def escopo():
    global x
    x = 10

    def outra_funcao():
        x= 11
        y = 2
        print(x, y)

    outra_funcao()
    print(x)

print(x)
escopo()
print(x)