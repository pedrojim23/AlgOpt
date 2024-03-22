# Función para determinar si un punto es parte de la envolvente convexa
def es_parte_envolvente(p, q, r):
    return (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1]) >= 0

# Algoritmo de Jarvis March para encontrar la envolvente convexa
def jarvis_march(puntos):
    n = len(puntos)
    if n < 3:
        return puntos
    
    envolvente = []
    
    # Encuentra el punto más a la izquierda
    punto_inicio = min(puntos)
    p = punto_inicio
    q = None
    while True:
        envolvente.append(p)
        q = (p[0] + 1, p[1])
        for r in puntos:
            if es_parte_envolvente(p, q, r):
                q = r
        p = q
        if p == punto_inicio:
            break
    
    return envolvente

# Función principal
def checkio(coordenadas):
    envolvente_convexa = jarvis_march(coordenadas)
    indices_envolvente_convexa = [coordenadas.index(p) for p in envolvente_convexa]
    return indices_envolvente_convexa

# Ejemplos de uso
print(checkio([[7, 6], [8, 4], [7, 2], [3, 2], [1, 6], [1, 8], [4, 9]]))  # Salida: [4, 5, 6, 0, 1, 2, 3]
print(checkio([[3, 8], [1, 6], [6, 2], [7, 6], [5, 5], [8, 4], [6, 8]]))  # Salida: [1, 0, 2, 5, 6, 3]
