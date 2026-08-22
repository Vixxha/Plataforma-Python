# === METADATA ===
# title: Transponer Matriz 2D
# description: Escribe una función que reciba una matriz cuadrada (representada como una lista de listas) de tamaño N x N y devuelva su matriz transpuesta (intercambiando filas por columnas).
# difficulty: Intermedio
# expected_output: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
# hint: Puedes usar listas por comprensión combinadas con la función zip() para iterar sobre las columnas en lugar de las filas.

# === SOLUTION ===
def transponer_matriz(matriz):
    if not matriz:
        return []
    return [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]

# === TESTS ===
try:
    assert transponer_matriz([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [[1, 4, 7], [2, 5, 8], [3, 6, 9]], "Error: el test 1 ha fallado."
    assert transponer_matriz([[1, 2], [3, 4]]) == [[1, 3], [2, 4]], "Error: considera casos límites en tu lógica."
    assert transponer_matriz([[5]]) == [[5]], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")