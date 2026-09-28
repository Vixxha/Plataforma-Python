# === METADATA ===
# title: Operaciones Básicas en Matrices (Suma de Diagonales)
# description: Escribe una función que reciba una matriz cuadrada (representada como una lista de listas de números enteros) y devuelva la suma de los elementos que se encuentran en su diagonal principal.
# difficulty: Intermedio
# expected_output: 15
# hint: La diagonal principal de una matriz cuadrada está formada por los elementos donde el índice de la fila es igual al índice de la columna (matriz[i][i]).

# === SOLUTION ===
def suma_diagonal_principal(matriz):
    suma = 0
    for i in range(len(matriz)):
        suma += matriz[i][i]
    return suma

# === TESTS ===
try:
    assert suma_diagonal_principal([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 15, "Error: el test 1 ha fallado."
    assert suma_diagonal_principal([[5]]) == 5, "Error: considera casos límites en tu lógica."
    assert suma_diagonal_principal([[1, 0], [0, 1]]) == 2, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")