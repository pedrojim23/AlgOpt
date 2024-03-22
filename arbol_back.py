
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.children = []

def backtrack(node, path):
    # Hacer algo con el nodo actual, por ejemplo, imprimir su valor
    print(node.val)

    # Agregar el nodo actual al camino
    path.append(node.val)

    # Si el nodo actual es una solución, hacer algo con el camino encontrado
    if is_solution(node):
        process_solution(path)
    
    # Recorrer los hijos del nodo actual
    for child in node.children:
        # Si el hijo no está en el camino actual, explorarlo
        if child.val not in path:
            backtrack(child, path)
    
    # Retroceder: quitar el nodo actual del camino
    path.pop()

def is_solution(node):
    # Implementar la condición para determinar si el nodo es una solución
    # Por ejemplo, si es un nodo hoja
    return not node.children

def process_solution(path):
    # Hacer algo con el camino encontrado
    print("Solución encontrada:", path)

# Ejemplo de uso
# Crear un árbol de ejemplo
root = TreeNode(1)
root.children = [TreeNode(2), TreeNode(3)]
root.children[0].children = [TreeNode(4), TreeNode(5)]
root.children[1].children = [TreeNode(6), TreeNode(7)]

# Llamar a la función de backtracking
backtrack(root, [])
