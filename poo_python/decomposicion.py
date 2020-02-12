
class Auto:
    def __init__(self, modelo, marca, color):
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self._estado = 'en reposo'
        self._motor = Motor(cilindros=4)
        self.velociad = 0
        self._nitro = Motor.in_nitro(cantidad=0)

    def acelerar(self, tipo='despacio'):
        if tipo == 'rapido':
            self._motor.inyecta_gasolina(10)
            self.velociad = 100
        else:
            self._motor.inyecta_gasolina(3)
            self.velocidad = 20

        self._estado = 'En movimiento'
    
    
    def nitro(self):
        self._nitro(cantidad=20)

class Motor:
    def __init__(self, cilindros, tipo='gasolina'):
        self.cilindros = cilindros
        self.tipo = tipo
        self._temperatura = 0

    def inyecta_gasolina(self, cantidad):
        if cantidad >= 10:
            self._temperatura += 12
        
        else:
            self._temperatura += 5
    
    def in_nitro(self, cantidad):
        if cantidad == 20:
            self._temperatura += 10
            self.velociad += 20
        elif cantidad < 20:
            self._temperatura += 5
            self.velociad += 10
        
        else:
            self._temperatura += 0
            self.velociad += 0