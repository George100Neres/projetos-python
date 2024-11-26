# Operadores logicos
# and or not

entrada = input('[E]ntrar [S]air?: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'
# if True: 

if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')