# === METADATA ===
# title: Transponer y Filtrar Matriz
# description: Escribe una función que reciba una matriz (lista de listas) de números enteros y devuelva una nueva matriz transpuesta (intercambiando filas por columnas), pero omitiendo aquellos números que sean negativos.
# difficulty: Intermedio
# expected_output: [[1, 4], [2, 5]] para la entrada [[1, -2, 3], [4, 5, -6]]
# hint: Primero puedes transponer la matriz usando comprensión de listas y luego filtrar los valores negativos en cada fila resultante.

# === SOLUTION ===
def transponer_y_filtrar(matriz):
    if not matriz or not matriz[0]:
        return []
    
    filas = len(matriz)
    columnas = len(matriz[0])
    
    transpuesta = [[matriz[r][c] for r in range(filas)] for c in range(columnas)]
    
    resultado = [[x for x in fila if x >= 0] for fila in transpuesta]
    return resultado

# === TESTS ===
try:
    assert transponer_y_filtrar([[1, -2, 3], [4, 5, -6]]) == [[1, 4], [2, 5], [3]], "Error: el test 1 ha fallado."
    assert transponer_y_filtrar([[-1, -2], [-3, -4]]) == [[], []], "Error: considera casos límites en tu lógica."
    assert transponer_y_filtrar([[0, 2], [3, 4]]) == [[0, 3], [2, 4]], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")