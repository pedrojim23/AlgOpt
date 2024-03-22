class NodoArbol:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []

def backtrack(nodo, objetivo, camino, indent=''):
    # Hacer algo con el nodo actual, por ejemplo, imprimir su valor
    print(indent + '└─', nodo.valor)

    # Agregar el nodo actual al camino
    camino.append(nodo.valor)

    # Si el nodo actual es una solución, hacer algo con el camino encontrado
    if nodo.valor == objetivo:
        procesar_solucion(camino)
    
    # Recorrer los hijos del nodo actual
    for i, hijo in enumerate(nodo.hijos):
        # Si el hijo no está en el camino actual, explorarlo
        if hijo.valor not in camino:
            # Imprimir la conexión entre nodos
            print(indent + '  |')

            # Recursivamente explorar el hijo
            backtrack(hijo, objetivo, camino, indent + ('   ' if i == len(nodo.hijos) - 1 else '  |'))
    
    # Retroceder: quitar el nodo actual del camino
    camino.pop()

    # Si se ha explorado todo el árbol y no se ha encontrado una solución, imprimir un mensaje
    if nodo.valor == 1 and objetivo not in camino:
        print("No se encontró una solución para el objetivo", objetivo)



def procesar_solucion(camino):
    # Hacer algo con el camino encontrado
    print("Solución encontrada:", camino)

# Ejemplo de uso
# Crear un árbol de ejemplo
raiz = NodoArbol(1)
raiz.hijos = [NodoArbol(2), NodoArbol(3)]
raiz.hijos[0].hijos = [NodoArbol(4), NodoArbol(5)]
raiz.hijos[1].hijos = [NodoArbol(6), NodoArbol(7)]

# Especificar el nodo objetivo que se desea buscar
nodo_objetivo = 8

# Llamar a la función de backtracking con el nodo raíz y el nodo objetivo
backtrack(raiz, nodo_objetivo, [])
