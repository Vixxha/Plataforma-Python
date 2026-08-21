# === METADATA ===
# title: Matriz Transpuesta
# description: Escribe una función que reciba una matriz (lista de listas) representada como un vector de vectores de tamaño N x M y devuelva su matriz transpuesta (cambiar filas por columnas).
# difficulty: Intermedio
# expected_output: [[1, 4], [2, 5], [3, 6]]
# hint: Puedes usar listas por comprensión iterando sobre los índices de las columnas y luego sobre las filas de la matriz original.

# === SOLUTION ===
def matriz_transpuesta(matriz):
    if not matriz or not matriz[0]:
        return []
    
    filas = len(matriz)
    columnas = len(matriz[0])
    
    return [[matriz[i][j] for i in range(filas)] for j in range(columnas)]

# === TESTS ===
try:
    assert matriz_transpuesta([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]], "Error: el test 1 ha fallado."
    assert matriz_transpuesta([[1, 2], [3, 4]]) == [[1, 3], [2, 4]], "Error: considera casos límites en tu lógica."
    assert matriz_transpuesta([[5]]) == [[5]], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")