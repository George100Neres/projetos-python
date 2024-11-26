
# Voce trabalha em uma madereira e lida com os pedidos dos clientes. Você tem três pedidos
#para realizar no dia e seu gerente pediu para vocÊ selecionar peiddo para fazre a primeira
#entrega. Cada peiddo e uma lista com os códigos dos produtos que devem ser
#entregue. Por ser uma situação corriqueira voce deve criar uma função que automatiza esse processo.

#Dica: Crie variaveis em listas e depois uma função que compare as variaveis.

a = [1, 2, 3, 4, 5, 6]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]

def maior_pedido(a, b, c):
    maior_3 = 0 #sera o contador
    if a > b:
        if a > c:
            maior_3 = c
        else:
            maior_3 = a
    else:
        if b > c:
            maior_3 = b
    else:
        maior_3 = c
    return maior_3
  



