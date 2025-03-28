from punto_constructor import Punto
from rectangulo import Rectangulo
import math

def distancia(p1, p2):
    """Calcula la distancia entre dos puntos."""
    return math.sqrt((p2.x - p1.x)**2 + (p2.y - p1.y)**2)

def main():
    # Crear los puntos A, B, C y D
    A = Punto(2, 3)
    B = Punto(5, 5)
    C = Punto(-3, -1)
    D = Punto(0, 0)

    # Imprimir los puntos
    print("=== Puntos ===")
    print(f"A: {A}")
    print(f"B: {B}")
    print(f"C: {C}")
    print(f"D: {D}")
    print()

    # Consultar a qué cuadrante pertenecen los puntos A, C y D
    print("=== Cuadrantes ===")
    print(f"A está en el: {A.cuadrante()}")
    print(f"C está en el: {C.cuadrante()}")
    print(f"D está en el: {D.cuadrante()}")
    print()

    # Consultar los vectores AB y BA
    print("=== Vectores ===")
    print(f"Vector AB: {A.vector(B)}")
    print(f"Vector BA: {B.vector(A)}")
    print()

    # Consultar la distancia entre los puntos A y B, y B y A (opcional)
    print("=== Distancias ===")
    print(f"Distancia entre A y B: {distancia(A, B):.2f}")
    print(f"Distancia entre B y A: {distancia(B, A):.2f}")
    print()

    # Determinar cuál de los puntos A, B o C está más lejos del origen (opcional)
    print("=== Punto más lejano del origen ===")
    distancias = {
        "A": distancia(A, D),
        "B": distancia(B, D),
        "C": distancia(C, D)
    }
    punto_mas_lejano = max(distancias, key=distancias.get)
    print(f"El punto más lejano del origen es: {punto_mas_lejano}")
    print()

    # Crear un rectángulo utilizando los puntos A y B
    rectangulo = Rectangulo(A, B)

    # Consultar la base, altura y área del rectángulo
    print("=== Rectángulo ===")
    print(f"Base: {rectangulo.base()}")
    print(f"Altura: {rectangulo.altura()}")
    print(f"Área: {rectangulo.area()}")

if __name__ == "__main__":
    main()