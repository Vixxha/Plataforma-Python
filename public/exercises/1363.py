# === METADATA ===
# title: Matriz Transpuesta de 2x2
# description: Escribe una función que reciba una matriz de 2x2 (representada como una lista de listas) y devuelva su matriz transpuesta, es decir, aquella donde las filas se convierten en columnas.
# difficulty: Básico
# expected_output: [[1, 3], [2, 4]]
# hint: Recuerda que el elemento en la posición [i][j] de la matriz original debe pasar a la posición [j][i] en la nueva matriz.

# === SOLUTION ===
def transponer_matriz_2x2(matriz):
    return [
        [matriz[0][0], matriz[1][0]],
        [matriz[0][1], matriz[1][1]]
    ]

# === TESTS ===
try:
    assert transponer_matriz_2x2([[1, 2], [3, 4]]) == [[1, 3], [2, 4]], "Error: el test 1 ha fallado."
    assert transponer_matriz_2x2([[5, 6], [7, 8]]) == [[5, 7], [6, 8]], "Error: considera casos límites en tu lógica."
    assert transponer_matriz_2x2([[0, 1], [1, 0]]) == [[0, 1], [1, 0]], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")