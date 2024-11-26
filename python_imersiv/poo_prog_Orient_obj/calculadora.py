
class Calculadora:

    def calcular(self, op, num1, num2):
        if op  == '+':
         return self.__adicionar(num1, num2)
        elif op == '-':
         return  self .__subtrair(num1, num2)
        else:
            print('Operacao invalida')

    def __adicionar(num1, num2):
        return num1 + num2
    
    def __subtrair(num1, num2):
        return num1 - num2
    
# Instancias Calculadora
calculadora = Calculadora()
resultado = calculadora.calcular('+', 3, 2)
print(resultado)