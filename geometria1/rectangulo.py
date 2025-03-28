from punto_constructor import Punto

class Rectangulo:
    def __init__(self, punto_inicial=None, punto_final=None):
        """Constructor que inicializa los puntos de la diagonal del rectángulo."""
        self.punto_inicial = punto_inicial if punto_inicial else Punto(0, 0)
        self.punto_final = punto_final if punto_final else Punto(0, 0)

    def base(self):
        """Calcula y devuelve la base del rectángulo."""
        return abs(self.punto_final.x - self.punto_inicial.x)

    def altura(self):
        """Calcula y devuelve la altura del rectángulo."""
        return abs(self.punto_final.y - self.punto_inicial.y)

    def area(self):
        """Calcula y devuelve el área del rectángulo."""
        return self.base() * self.altura()