# === METADATA ===
# title: Transponer Matriz 2D
# description: Escribe una función que reciba una matriz (lista de listas) de dimensiones $N \times M$ y devuelva su matriz transposta ($M \times N$), donde las filas de la matriz original se convierten en las columnas de la nueva matriz.
# difficulty: Intermedio
# expected_output: [[1, 4], [2, 5], [3, 6]]
# hint: Puedes usar la comprensión de listas recorriendo los índices de las columnas y luego las filas, o iterar usando zip(*matriz).

# === SOLUTION ===
def transponer_matriz(matriz):
    if not matriz or not matriz[0]:
        return []
    
    filas = len(matriz)
    columnas = len(matriz[0])
    
    matriz_transpuesta = [[matriz[i][j] for i in range(filas)] for j in range(columnas)]
    return matriz_transpuesta

# === TESTS ===
try:
    assert transponer_matriz([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]], "Error: el test 1 ha fallado."
    assert transponer_matriz([[1, 2], [3, 4]]) == [[1, 3], [2, 4]], "Error: considera casos límites en tu lógica."
    assert transponer_matriz([[5]]) == [[5]], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")