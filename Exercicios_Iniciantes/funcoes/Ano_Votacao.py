# Cire um programa que tenha uma função chamada voto() que vai receber omo 
#parametro o ano de nascimento de uma pessoa, retornando um valor literal
# indicando se uma pessoa tem coto NEGADO, OPCIONAL ou OBRIGAOTRIO nas eleicoes

def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'
    
   # Programa pincipal
nasc = int(input("Em qual an você nasceu? "))
print(voto(nasc))

