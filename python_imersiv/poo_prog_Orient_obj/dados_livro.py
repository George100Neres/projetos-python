class Livro:
    def __init__(self, titulo, autor, num_paginas, genero):
        self.titulo = titulo
        self.autor = autor
        self.num_paginas = num_paginas
        self.egnero = genero

    def get_titulo(self):
        return self.titulo
    
    def get_titulo(self, titulo):
        return self.titulo   
    
meu_livro = Livro(titulo="crepusculo", autor="sephenie", num_paginas=200, genero="romance")

print("titulo do livro: ", meu_livro.get_titulo())

meu_livro.seu_titulo(titulo="Lua Nova")

print("Novo Titulo do Livro: ", meu_livro.get_titulo())