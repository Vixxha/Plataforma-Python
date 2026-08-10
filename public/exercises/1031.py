# === METADATA ===
# title: Transponer Matriz 2D
# description: Escribe una función que reciba una matriz (lista de listas) de dimensiones N x M y devuelva su matriz transpuesta (intercambiando filas por columnas).
# difficulty: Intermedio
# expected_output: [[1, 4], [2, 5], [3, 6]]
# hint: Puedes recorrer los índices de columnas y filas, o utilizar una comprensión de listas avanzada combinando 'zip'.

# === SOLUTION ===
def transponer_matriz(matriz):
    if not matriz or not matriz[0]:
        return []
    return [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]

# === TESTS ===
try:
    assert transponer_matriz([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]], "Error: el test 1 ha fallado."
    assert transponer_matriz([[1, 2], [3, 4]]) == [[1, 3], [2, 4]], "Error: considera casos límites en tu lógica."
    assert transponer_matriz([[5]]) == [[5]], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")