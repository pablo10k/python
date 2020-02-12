

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def avanzar(self):
        print('Caminando!')
    
class Ciclista(Persona):
    def __init__(self, nombre):
        super().__init__(nombre)
    
    #polimorfismo
    def avanzar(self):
        print('Pedaleando!')
    #

def main():
    persona = Persona('Pablo')
    persona.avanzar()

    ciclista = Ciclista('Pablo')
    ciclista.avanzar()
if __name__ == "__main__":
    main()