# -*- coding: utf-8 -*-

class Lapiz:
    def __init__(self, tamaño, color, material):
        self.tamaño = tamaño
        self.color = color
        self.material = material

    def escribir(self, texto):
        return print(texto)

class Grafito(Lapiz):
    def __init__(self, tamaño, color, material):
        super().__init__(tamaño, color, material)
    
class Pasta(Lapiz):
    def __init__(self, tamaño, color, material='plastico'):
        super().__init__(tamaño, color, material)

if __name__ == "__main__":
    lapiz_grafito = Grafito('grande', 'azul', 'madera')
    lapiz_grafito.escribir('Escribiendo a grafito')

    lapiz_pasta = Pasta('pequeño', 'rojo', 'plastico')
    lapiz_pasta.escribir('Escriendo a lapiz pasta')