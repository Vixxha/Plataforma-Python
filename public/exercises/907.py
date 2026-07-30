# === METADATA ===
# title: Diagonal Principal de una Matriz Cuadrada
# description: Escribe una función que reciba una matriz cuadrada (representada como una lista de listas) y retorne una nueva lista que contenga los elementos de su diagonal principal (aquellos donde el índice de la fila es igual al índice de la columna).
# difficulty: Intermedio
# expected_output: [1, 5, 9]
# hint: Puedes recorrer la matriz usando un bucle con un índice único 'i' para acceder a la posición matriz[i][i].

# === SOLUTION ===
def obtener_diagonal_principal(matriz):
    diagonal = []
    for i in range(len(matriz)):
        diagonal.append(matriz[i][i])
    return diagonal

# === TESTS ===
try:
    assert obtener_diagonal_principal([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 5, 9], "Error: el test 1 ha fallado."
    assert obtener_diagonal_principal([[10, 20], [30, 40]]) == [10, 40], "Error: considera casos límites en tu lógica."
    assert obtener_diagonal_principal([[5]]) == [5], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")