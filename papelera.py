from ortools.linear_solver import pywraplp


def create_data_model():
    """Create the data for the example."""
    data = {}
    weights = [48, 30, 19, 36, 36, 27, 42, 42, 36, 24, 30]
    data["weights"] = weights
    data["items"] = list(range(len(weights)))
    data["bins"] = data["items"]
    data["bin_capacity"] = 100
    return data



def main():
    #Crear los datos del problema.
    data = create_data_model()

    # Create the mip solver with the SCIP backend.
    solver = pywraplp.Solver.CreateSolver("SCIP")

    if not solver:
        return

    # Variables
    # x[i, j] = 1 if item i is packed in bin j.
    x = {}
    for i in data["items"]:
        for j in data["bins"]:
            x[(i, j)] = solver.IntVar(0, 1, "x_%i_%i" % (i, j))

    # y[j] = 1 if bin j is used.
    y = {}
    for j in data["bins"]:
        y[j] = solver.IntVar(0, 1, "y[%i]" % j)

    # Constraints
    # Each item must be in exactly one bin.
    for i in data["items"]:
        solver.Add(sum(x[i, j] for j in data["bins"]) == 1)

    # The amount packed in each bin cannot exceed its capacity.
    for j in data["bins"]:
        solver.Add(
            sum(x[(i, j)] * data["weights"][i] for i in data["items"])
            <= y[j] * data["bin_capacity"]
        )

    # Objective: minimize the number of bins used.
    solver.Minimize(solver.Sum([y[j] for j in data["bins"]]))

    print(f"Solving with {solver.SolverVersion()}")
    status = solver.Solve()

    #Verifica si la solución encontrada es óptima.
    if status == pywraplp.Solver.OPTIMAL:
        num_bins = 0
        #Itera sobre todos los contenedores posibles.
        for j in data["bins"]:
            #Verifica si el contenedor j está en uso.
            if y[j].solution_value() == 1:
                #Inicializa variables para los ítems empaquetados y el peso del contenedor actual.
                bin_items = []
                bin_weight = 0
                #Itera sobre todos los ítems.
                for i in data["items"]:
                    #Verifica si el ítem i está empaquetado en el contenedor j.
                    if x[i, j].solution_value() > 0:
                        bin_items.append(i)
                        #Actualiza la lista de ítems empaquetados y el peso del contenedor actual.
                        bin_weight += data["weights"][i]
                if bin_items:
                    #Si hay ítems empaquetados en el contenedor, incrementa el contador de contenedores.
                    num_bins += 1
                    print("Bin number", j)
                    print("  Items packed:", bin_items)
                    print("  Total weight:", bin_weight)
                    print()
        print()
        print("Number of bins used:", num_bins)
        print("Time = ", solver.WallTime(), " milliseconds")
    else:
        print("The problem does not have an optimal solution.")


if __name__ == "__main__":
    main()
 
 #Se verifica si la solución encontrada es óptima.
#Si es óptima, se itera sobre cada contenedor, identifica los contenedores utilizados y muestra la lista de ítems empaquetados en cada uno, junto con el peso total del contenedor.
#Se imprime el número total de contenedores utilizados y el tiempo que tomó resolver el problema.
#Si la solución no es óptima, se imprime un mensaje indicando que el problema no tiene una solución óptima.
