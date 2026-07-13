# === METADATA ===
# title: Filtro de Matrices Cuadradas
# description: Crea una función que reciba una matriz cuadrada (lista de listas) y devuelva una nueva lista conteniendo únicamente los elementos de la diagonal principal.
# difficulty: Intermedio
# expected_output: [1, 5, 9] para una matriz 3x3 con valores del 1 al 9.
# hint: Utiliza un bucle for con un único índice que recorra tanto la fila como la columna simultáneamente (ej: matriz[i][i]).

# === SOLUTION ===
def obtener_diagonal(matriz):
    diagonal = []
    for i in range(len(matriz)):
        diagonal.append(matriz[i][i])
    return diagonal

# === TESTS ===
try:
    assert obtener_diagonal([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 5, 9], "Error: el test 1 ha fallado."
    assert obtener_diagonal([[10, 20], [30, 40]]) == [10, 40], "Error: considera casos límites en tu lógica."
    assert obtener_diagonal([[5]]) == [5], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")