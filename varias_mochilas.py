"""Solves a multiple knapsack problem using the CP-SAT solver."""
from ortools.sat.python import cp_model


def main():

    #Datos del problema(peso y valores).
    data = {}
    data["weights"] = [48, 30, 42, 36, 36, 48, 42, 42, 36, 24, 30, 30, 42, 36, 36]
    data["values"] = [10, 30, 25, 50, 35, 30, 15, 40, 30, 35, 45, 10, 20, 30, 25]

    #Asegurar que la cantidad de pesos sea igual a la cantidad de valores.
    assert len(data["weights"]) == len(data["values"])

    #Calcula el número total de ítems en la mochila basado en la longitud de la lista de pesos.
    data["num_items"] = len(data["weights"])
    #Crea un conjunto de índices que representa todos los ítems posibles en la mochila.
    data["all_items"] = range(data["num_items"])

    #Lista que representa las capacidades de cada mochila.
    data["bin_capacities"] = [100, 100, 100, 100, 100]
    #Calcula el número total de mochilas basado en la longitud de la lista de capacidades.
    data["num_bins"] = len(data["bin_capacities"])
    #Crea un conjunto de índices que representa todas las mochilas posibles.
    data["all_bins"] = range(data["num_bins"])

    model = cp_model.CpModel()

    # Variables.
    # x[i, b] = 1 if item i is packed in bin b.
    x = {}
    for i in data["all_items"]:
        for b in data["all_bins"]:
            x[i, b] = model.NewBoolVar(f"x_{i}_{b}")

    # Constraints.
    # Each item is assigned to at most one bin.
    for i in data["all_items"]:
        model.AddAtMostOne(x[i, b] for b in data["all_bins"])

    # The amount packed in each bin cannot exceed its capacity.
    for b in data["all_bins"]:
        model.Add(
            sum(x[i, b] * data["weights"][i] for i in data["all_items"])
            <= data["bin_capacities"][b]
        )

    # Objective.
    # Maximize total value of packed items.
    objective = []
    for i in data["all_items"]:
        for b in data["all_bins"]:
            objective.append(cp_model.LinearExpr.Term(x[i, b], data["values"][i]))
    model.Maximize(cp_model.LinearExpr.Sum(objective))

    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    #Verifica si la solución encontrada es óptima.
    if status == cp_model.OPTIMAL:
    #Imprime el valor total de los elementos empaquetados.
        print(f"Total packed value: {solver.ObjectiveValue()}")
        #Inicializa la variable para almacenar el peso total empaquetado.
        total_weight = 0
        #Itera sobre todas las mochilas
        for b in data["all_bins"]:
            print(f"Bin {b}")
            bin_weight = 0
            bin_value = 0
            #Itera sobre todos los ítems.
            for i in data["all_items"]:
                #Verifica si el ítem i está empaquetado en la mochila b.
                if solver.Value(x[i, b]) > 0:
                    #Imprime información sobre el ítem empaquetado.
                    print(
                        f"Item {i} weight: {data['weights'][i]} value: {data['values'][i]}"
                    )
                    #Actualiza el peso y valor de la mochila actual.
                    bin_weight += data["weights"][i]
                    bin_value += data["values"][i]
            #Imprime el peso y valor total de la mochila actual.
            print(f"Packed bin weight: {bin_weight}")
            print(f"Packed bin value: {bin_value}\n")
            #Actualiza el peso total empaquetado.
            total_weight += bin_weight
        #Imprime el peso total empaquetado de todas las mochilas.
        print(f"Total packed weight: {total_weight}")
    else:
        print("The problem does not have an optimal solution.")


if __name__ == "__main__":
    main()
