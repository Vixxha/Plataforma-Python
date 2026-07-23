# === METADATA ===
# title: Transponer y Filtrar Matriz
# description: Escribe una función que reciba una matriz (lista de listas) de números enteros y devuelva una nueva matriz transpuesta (intercambiando filas por columnas) pero donde solo se incluyan aquellas columnas cuya suma total sea mayor o igual a un valor umbral dado.
# difficulty: Intermedio
# expected_output: [[1, 4], [2, 5], [3, 6]]
# hint: Primero calcula la matriz transpuesta y luego evalúa la suma de cada nueva fila (que corresponde a las columnas originales) antes de construir la matriz resultante.

# === SOLUTION ===
def transponer_y_filtrar(matriz, umbral):
    if not matriz or not matriz[0]:
        return []
    
    filas = len(matriz)
    columnas = len(matriz[0])
    
    # Obtener la matriz transpuesta
    transpuesta = [[matriz[r][c] for r in range(filas)] for c in range(columnas)]
    
    # Filtrar las filas de la transpuesta cuya suma sea >= umbral
    resultado = [fila for fila in transpuesta if sum(fila) >= umbral]
    
    return resultado

# === TESTS ===
try:
    assert transponer_y_filtrar([[1, 2, 3], [4, 5, 6]], 5) == [[1, 4], [2, 5], [3, 6]], "Error: el test 1 ha fallado."
    assert transponer_y_filtrar([[1, 1], [1, 1]], 5) == [], "Error: considera casos límites en tu lógica."
    assert transponer_y_filtrar([[10, 2], [5, 5]], 10) == [[10, 5]], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")