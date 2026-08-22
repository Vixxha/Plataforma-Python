# === METADATA ===
# title: Matriz Transpuesta de 2x2
# description: Escribe una función que reciba una matriz (lista de listas) de 2x2 y devuelva su matriz transpuesta, es decir, aquella donde las filas se convierten en columnas y las columnas en filas.
# difficulty: Intermedio
# expected_output: [[1, 3], [2, 4]]
# hint: Puedes construir una nueva lista accediendo a los elementos cruzados de la matriz original: matriz[0][1] pasa a ser el nuevo elemento [1][0].

# === SOLUTION ===
def matriz_transpuesta_2x2(matriz):
    return [
        [matriz[0][0], matriz[1][0]],
        [matriz[0][1], matriz[1][1]]
    ]

# === TESTS ===
try:
    assert matriz_transpuesta_2x2([[1, 2], [3, 4]]) == [[1, 3], [2, 4]], "Error: el test 1 ha fallado."
    assert matriz_transpuesta_2x2([[5, 6], [7, 8]]) == [[5, 7], [6, 8]], "Error: considera casos límites en tu lógica."
    assert matriz_transpuesta_2x2([[0, 1], [1, 0]]) == [[0, 1], [1, 0]], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")