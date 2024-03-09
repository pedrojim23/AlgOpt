import heapq
'''
def dijkstra(graph, inicio):
    distancias = {nodo: float('inf') for nodo in graph}
    distancias[inicio] = 0
    cola_prioridad = [(0, inicio)]

    while cola_prioridad:
        distancia_actual, nodo_actual = heapq.heappop(cola_prioridad)

        if distancia_actual > distancias[nodo_actual]:
            continue

        for vecino, peso in graph[nodo_actual].items():
            distancia = distancia_actual + peso
            if distancia < distancias[vecino]:
                distancias[vecino] = distancia
                heapq.heappush(cola_prioridad, (distancia, vecino))

    return distancias

grafo = {
    'A': {'B': 2, 'D': 5},
    'B': {'C': 3, 'E': 2},
    'C': {'Z': 7},
    'D': {'E': 1, 'F': 6},
    'E': {'G': 2, 'H': 5},
    'F': {'Z': 5},
    'G': {'Z': 3},
    'H': {'I': 4},
    'I': {'Z': 1},
    'Z': {}
}

nodo_inicio = 'A'

resultado = dijkstra(grafo, nodo_inicio)

for nodo, distancia in resultado.items():
    print(f'Distancia desde {nodo_inicio} hasta {nodo}: {distancia}')

'''


def dijkstra(graph, start, end):
    # Inicializar distancias y nodos anteriores
    distancias = {nodo: float('infinity') for nodo in graph}
    distancias[start] = 0
    nodos_anteriores = {nodo: None for nodo in graph}
    cola_prioridad = [(0, start)]

    while cola_prioridad:
        distancia_actual, nodo_actual = heapq.heappop(cola_prioridad)

        if distancia_actual > distancias[nodo_actual]:
            continue

        for vecino, peso in graph[nodo_actual].items():
            distancia = distancia_actual + peso
            if distancia < distancias[vecino]:
                distancias[vecino] = distancia
                nodos_anteriores[vecino] = nodo_actual
                heapq.heappush(cola_prioridad, (distancia, vecino))

    # Construir el camino desde el nodo de inicio hasta el nodo destino
    camino = []
    actual = end
    while actual is not None:
        camino.insert(0, actual)
        actual = nodos_anteriores[actual]

    return distancias, camino

# Definir el grafo
grafo = {
    'A': {'B': 2, 'D': 5},
    'B': {'C': 3, 'E': 2},
    'C': {'Z': 7},
    'D': {'E': 1, 'F': 6},
    'E': {'G': 2, 'H': 5},
    'F': {'Z': 5},
    'G': {'Z': 3},
    'H': {'I': 4},
    'I': {'Z': 1},
    'Z': {}
}

nodo_inicio = 'A'
nodo_destino = 'Z'

# Obtener resultados de Dijkstra
distancias, camino = dijkstra(grafo, nodo_inicio, nodo_destino)

# Imprimir resultados
print(f"Distancia desde {nodo_inicio} hasta {nodo_destino}: {distancias[nodo_destino]}")
print(f"Camino más corto: {' -> '.join(camino)}")
