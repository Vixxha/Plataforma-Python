# === METADATA ===
# title: Transponer Matriz 2D
# description: Escribe una función que reciba una matriz (lista de listas) de dimensiones $N \times M$ y devuelva su matriz transposta (intercambiando filas por columnas).
# difficulty: Intermedio
# expected_output: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
# hint: Puedes usar la comprensión de listas recorriendo los índices de las columnas primero y luego las filas, o iterar sobre un rango basado en las dimensiones de la matriz.

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
    assert transponer_matriz([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [[1, 4, 7], [2, 5, 8], [3, 6, 9]], "Error: el test 1 ha fallado."
    assert transponer_matriz([[1, 2], [3, 4], [5, 6]]) == [[1, 3, 5], [2, 4, 6]], "Error: considera casos límites en tu lógica."
    assert transponer_matriz([[1]]) == [[1]], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")