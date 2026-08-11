# === METADATA ===
# title: Transponer Matriz 2D
# description: Escribe una función que reciba una matriz (lista de listas) de dimensiones M x N y devuelva su matriz transpuesta (N x M), es decir, intercambiando filas por columnas.
# difficulty: Intermedio
# expected_output: [[1, 4], [2, 5], [3, 6]]
# hint: Puedes utilizar listas por comprensión anidadas recorriendo los índices de las columnas y filas originales, o la función zip(*matriz).

# === SOLUTION ===
def transponer_matriz(matriz):
    if not matriz or not matriz[0]:
        return []
    return [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]

# === TESTS ===
try:
    assert transponer_matriz([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]], "Error: el test 1 ha fallado."
    assert transponer_matriz([[1]]) == [[1]], "Error: considera casos límites en tu lógica."
    assert transponer_matriz([[1, 2], [3, 4], [5, 6]]) == [[1, 3, 5], [2, 4, 6]], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")