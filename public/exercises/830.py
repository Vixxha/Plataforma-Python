# === METADATA ===
# title: Transponer una Matriz
# description: Escribe una función que reciba una matriz (lista de listas) de dimensiones m x n y devuelva su matriz transpuesta (n x m), donde las filas se convierten en columnas y viceversa.
# difficulty: Intermedio
# expected_output: [[1, 4], [2, 5], [3, 6]]
# hint: Puedes utilizar listas por comprensión anidadas o recorrer los índices de columnas y filas iterativamente.

# === SOLUTION ===
def transponer_matriz(matriz):
    if not matriz or not matriz[0]:
        return []
    
    filas = len(matriz)
    columnas = len(matriz[0])
    
    matriz_transpuesta = [[matriz[j][i] for j in range(filas)] for i in range(columnas)]
    return matriz_transpuesta

# === TESTS ===
try:
    assert transponer_matriz([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]], "Error: el test 1 ha fallado."
    assert transponer_matriz([[1, 2], [3, 4]]) == [[1, 3], [2, 4]], "Error: considera casos límites en tu lógica."
    assert transponer_matriz([[5]]) == [[5]], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")