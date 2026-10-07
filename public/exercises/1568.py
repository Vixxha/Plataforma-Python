# === METADATA ===
# title: Transponer una Matriz y Sumar Filas
# description: Escribe una función que reciba una matriz (lista de listas) de dimensiones N x M, calcule su matriz transpuesta (intercambiando filas por columnas) y finalmente devuelva una lista con la suma de los elementos de cada fila de la matriz transpuesta.
# difficulty: Intermedio
# expected_output: [6, 15, 24] para la matriz [[1, 2, 3], [4, 5, 6]]
# hint: Recuerda que puedes acceder a las columnas usando bucles anidados o comprensiones de listas, donde las columnas de la original se convierten en las filas de la transpuesta.

# === SOLUTION ===
def transponer_y_sumar_filas(matriz):
    if not matriz or not matriz[0]:
        return []
    
    filas = len(matriz)
    columnas = len(matriz[0])
    
    transpuesta = [[matriz[f][c] for f in range(filas)] for c in range(columnas)]
    
    return [sum(fila) for fila in transpuesta]

# === TESTS ===
try:
    assert transponer_y_sumar_filas([[1, 2, 3], [4, 5, 6]]) == [5, 7, 9], "Error: el test 1 ha fallado."
    assert transponer_y_sumar_filas([[10, 20], [30, 40], [50, 60]]) == [90, 120], "Error: considera casos límites en tu lógica."
    assert transponer_y_sumar_filas([[5]]) == [5], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")