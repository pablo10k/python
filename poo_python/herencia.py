
class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def area(self):
        return self.base * self.altura

class Cuadrado(Rectangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)
            #se le da lado como base y altura
            #al constructor de Rectangulo
            #con super se heredan todos los metodos
            #en Rectangulo

if __name__ == "__main__":
    rectangulo = Rectangulo(base=5, altura=10)
    print(rectangulo.area())

    cuadrado = Cuadrado(lado=10)
    print(cuadrado.area())
    #llamo al metodo area en Rectangulo el cual
    #se heredo a Cuadrado