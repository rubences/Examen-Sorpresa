def determinar_cuadrante(punto):
    if punto.x > 0 and punto.y > 0:
        return "Primer cuadrante"
    elif punto.x < 0 and punto.y > 0:
        return "Segundo cuadrante"
    elif punto.x < 0 and punto.y < 0:
        return "Tercer cuadrante"
    elif punto.x > 0 and punto.y < 0:
        return "Cuarto cuadrante"
    elif punto.x == 0 and punto.y != 0:
        return "Eje Y"
    elif punto.y == 0 and punto.x != 0:
        return "Eje X"
    else:
        return "Origen"