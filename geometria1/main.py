from punto_constructor import Punto
from rectangulo import Rectangulo
import math

def distancia(p1, p2):
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

    # Consultar a qué cuadrante pertenecen los puntos A, B, C y D
    print("=== Cuadrantes ===")
    print(f"A está en el: {A.cuadrante()}")
    print(f"C está en el: {C.cuadrante()}")
    print(f"D está en el: {D.cuadrante()}")
    print()

    # Consultar los vectores AB y BA
    print("=== Vectores ===")
    vector_AB = A.vector(B)
    vector_BA = B.vector(A)
    print(f"Vector AB: ({B.x} - {A.x}, {B.y} - {A.y}) = {vector_AB}")
    print(f"Vector BA: ({A.x} - {B.x}, {A.y} - {B.y}) = {vector_BA}")
    print()

    # Consultar la distancia entre los puntos A y B, y B y A (opcional)
    print("=== Distancias ===")
    distancia_AB = distancia(A, B)
    distancia_BA = distancia(B, A)
    print("Fórmula para calcular la distancia entre dos puntos:")
    print("Distancia = √((x2 - x1)² + (y2 - y1)²)")
    print(f"Distancia entre A y B: √(({B.x} - {A.x})² + ({B.y} - {A.y})²) = √({(B.x - A.x)**2} + {(B.y - A.y)**2}) = {distancia_AB:.2f}")
    print(f"Distancia entre B y A: √(({A.x} - {B.x})² + ({A.y} - {B.y})²) = √({(A.x - B.x)**2} + {(A.y - B.y)**2}) = {distancia_BA:.2f}")
    print()

    # Determinar cuál de los puntos A, B o C está más lejos del origen (opcional)
    print("=== Punto más lejano del origen ===")
    distancia_A_origen = distancia(A, D)
    distancia_B_origen = distancia(B, D)
    distancia_C_origen = distancia(C, D)
    print(f"Distancia de A al origen: √(({A.x} - {D.x})² + ({A.y} - {D.y})²) = {distancia_A_origen:.2f}")
    print(f"Distancia de B al origen: √(({B.x} - {D.x})² + ({B.y} - {D.y})²) = {distancia_B_origen:.2f}")
    print(f"Distancia de C al origen: √(({C.x} - {D.x})² + ({C.y} - {D.y})²) = {distancia_C_origen:.2f}")
    distancias = {
        "A": distancia_A_origen,
        "B": distancia_B_origen,
        "C": distancia_C_origen
    }
    punto_mas_lejano = max(distancias, key=distancias.get)
    print(f"El punto más lejano del origen es: {punto_mas_lejano}")
    print()

    # Crear un rectángulo utilizando los puntos A y B
    rectangulo = Rectangulo(A, B)


    # Consultar la base, altura y área del rectángulo
    print("=== Rectángulo ===")
    base = rectangulo.base()
    altura = rectangulo.altura()
    area = rectangulo.area()
    print(f"Base: |{B.x} - {A.x}| = {base}")
    print(f"Altura: |{B.y} - {A.y}| = {altura}")
    print(f"Área: {base} * {altura} = {area}")

if __name__ == "__main__":
    main()