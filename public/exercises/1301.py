# === METADATA ===
# title: Transponer y Filtrar Matriz
# description: Escribe una función que reciba una matriz (lista de listas) de números enteros y devuelva una nueva matriz donde se hayan eliminado todas las filas que contengan al menos un número negativo. Además, la matriz resultante debe estar transonpuesta (intercambiar filas por columnas).
# difficulty: Intermedio
# expected_output: [[1, 4], [2, 5], [3, 6]]
# hint: Primero filtra las filas que no tengan números negativos, y luego calcula la transpuesta usando bucles o comprensión de listas.

# === SOLUTION ===
def transponer_y_filtrar(matriz):
    if not matriz or not matriz[0]:
        return []
    
    # Filtrar filas sin números negativos
    filas_validas = [fila for fila in matriz if all(x >= 0 for x in fila)]
    
    if not filas_validas:
        return []
    
    # Transponer la matriz filtrada
    filas = len(filas_validas)
    columnas = len(filas_validas[0])
    
    transpuesta = [[filas_validas[r][c] for r in range(filas)] for c in range(columnas)]
    
    return transpuesta

# === TESTS ===
try:
    assert transponer_y_filtrar([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]], "Error: el test 1 ha fallado."
    assert transponer_y_filtrar([[1, -2, 3], [4, 5, 6]]) == [[4], [5], [6]], "Error: considera casos límites en tu lógica."
    assert transponer_y_filtrar([[-1, -2], [-3, -4]]) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")