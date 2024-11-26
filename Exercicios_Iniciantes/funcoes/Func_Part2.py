#     Inicio| Fim | Incrementador
def contador(i, f, p):
    c = i
    while c <= f:
        print(f'{c} ', end="")
        c += p
    print('FIM!')

# IRa pular de 10 em dez
contador(0, 100, 10)
