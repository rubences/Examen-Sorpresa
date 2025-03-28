class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def cuadrante(self):
        if self.x > 0 and self.y > 0:
            return "Primer cuadrante"
        elif self.x < 0 and self.y > 0:
            return "Segundo cuadrante"
        elif self.x < 0 and self.y < 0:
            return "Tercer cuadrante"
        elif self.x > 0 and self.y < 0:
            return "Cuarto cuadrante"
        elif self.x == 0 and self.y != 0:
            return "Eje Y"
        elif self.y == 0 and self.x != 0:
            return "Eje X"
        else:
            return "Origen"
    
    def vector(self, otro_punto):
        return (otro_punto.x - self.x, otro_punto.y - self.y)

import math

def calcular_distancia(punto1, punto2):
    return math.sqrt((punto2.x - punto1.x)**2 + (punto2.y - punto1.y)**2)