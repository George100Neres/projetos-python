class MinhaClasse:

    def meu_metodo(self):
        print('Estou no metodo!')

    def meu_metodo2(self, num, mult):
        return num * mult
    
objeto = MinhaClasse()
result = objeto.meu_metodo2(3, 2)
print(result)
