# === METADATA ===
# title: Matriz Transpuesta
# description: Escribe una función que reciba una matriz (lista de listas) representada como un vector de vectores de tamaño N x M y devuelva su matriz transpuesta (de tamaño M x N), donde las filas se convierten en columnas.
# difficulty: Intermedio
# expected_output: [[1, 4], [2, 5], [3, 6]]
# hint: Puedes utilizar listas por comprensión iterando primero sobre las columnas (índices) y luego sobre las filas de la matriz original.

# === SOLUTION ===
def transponer_matriz(matriz):
    if not matriz or not matriz[0]:
        return []
    
    filas = len(matriz)
    columnas = len(matriz[0])
    
    return [[matriz[i][j] for i in range(filas)] for j in range(columnas)]

# === TESTS ===
try:
    assert transponer_matriz([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]], "Error: el test 1 ha fallado."
    assert transponer_matriz([[1, 2], [3, 4], [5, 6]]) == [[1, 3, 5], [2, 4, 6]], "Error: considera casos límites en tu lógica."
    assert transponer_matriz([[7]]) == [[7]], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")