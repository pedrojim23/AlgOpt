import math

# Función para encontrar el punto más bajo
def punto_mas_bajo(puntos):
    punto_bajo = puntos[0]
    for punto in puntos[1:]:
        if punto[1] < punto_bajo[1] or (punto[1] == punto_bajo[1] and punto[0] < punto_bajo[0]):
            punto_bajo = punto
    return punto_bajo

# Función para calcular el ángulo polar
def calcular_angulo_polar(p0, p1):
    dx = p1[0] - p0[0]
    dy = p1[1] - p0[1]
    return math.atan2(dy, dx)

# Función para determinar si tres puntos forman una esquina convexa
def forma_esquina_convexa(pila, p):
    if len(pila) < 2:
        return True
    dx1 = pila[-1][0] - pila[-2][0]
    dy1 = pila[-1][1] - pila[-2][1]
    dx2 = p[0] - pila[-1][0]
    dy2 = p[1] - pila[-1][1]
    return dx1 * dy2 - dy1 * dx2 >= 0

# Algoritmo de Graham Scan para encontrar la envolvente convexa
def graham_scan(puntos):
    if len(puntos) < 3:
        return puntos
    
    punto_base = punto_mas_bajo(puntos)
    puntos.sort(key=lambda p: (calcular_angulo_polar(punto_base, p), -p[1], p[0]))
    
    pila = [puntos[0], puntos[1]]
    
    for i in range(2, len(puntos)):
        while not forma_esquina_convexa(pila, puntos[i]):
            pila.pop()
        pila.append(puntos[i])
    
    return pila

# Función para obtener los índices de los puntos en la envolvente convexa
def obtener_indices_envolvente_convexa(envolvente, puntos):
    indices = []
    for punto_envolvente in envolvente:
        for i, punto in enumerate(puntos):
            if punto == punto_envolvente:
                indices.append(i)
                break
    return indices


# Función principal
def checkio(coordenadas):
    envolvente_convexa = graham_scan(coordenadas)
    indices_envolvente_convexa = obtener_indices_envolvente_convexa(envolvente_convexa, coordenadas)
    return indices_envolvente_convexa

# Ejemplos de uso
print(checkio([[7, 6], [8, 4], [7, 2], [3, 2], [1, 6], [1, 8], [4, 9]]))  # Salida: [4, 5, 6, 0, 1, 2, 3]
print(checkio([[3, 8], [1, 6], [6, 2], [7, 6], [5, 5], [8, 4], [6, 8]]))  # Salida: [1, 0, 2, 5, 6, 3]

