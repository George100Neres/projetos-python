# Chamada nome usuario

# 1 Maneira de importa o namespace
"""
import meu_namespace

# Ira printar o nome que esta declarado no arquivo (meu_namespace)
print(meu_namespace.nome_de_usuario)

mensagem = 'Bom dia, Fulano! Tudo bem?'

meu_namespace.funcao_do_namespace(mensagem)
"""

# 2 -Ira pegar tudo o que tem no arquivo meu_namespace

from meu_namespace import funcao_do_namespace

funcao_do_namespace(mensagem="Boa noite!")

