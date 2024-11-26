# Refatorar o seu codigo


def soma(x, y, z=None):
    if z is not None:
        print(f'{x=} {y=} {z=}', x + y + z)
    else:
        print(f'{x=} {y=}', x + y)

    
    soma(1, 2) #3
    soma(3, 5) # 8
    soma(100, 200) # 300
    soma(7, 9, 0) # 16

    

