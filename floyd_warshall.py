def floyd_warshall(graph):
    n = len(graph)
    
    # Inicializar la matriz de distancias con los pesos del grafo
    distancias = [fila[:] for fila in graph]

    # Iterar sobre todos los vértices intermedios
    for k in range(n):
        # Iterar sobre todos los nodos de origen
        for i in range(n):
            # Iterar sobre todos los nodos de destino
            for j in range(n):
                # Actualizar la distancia si encontramos un camino más corto a través de k
                distancias[i][j] = min(distancias[i][j], distancias[i][k] + distancias[k][j])

    return distancias

# Ejemplo de uso
grafo_ejemplo = [
    [0, 3, float('inf'), 7],
    [8, 0, 2, float('inf')],
    [5, float('inf'), 0, 1],
    [2, float('inf'), float('inf'), 0]
]


resultados = floyd_warshall(grafo_ejemplo)

# Mostrar los resultados
for fila in resultados:
    print(fila)
