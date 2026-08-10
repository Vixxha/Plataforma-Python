# === METADATA ===
# title: Transponer y Filtrar Matriz
# description: Escribe una función que reciba una matriz (lista de listas) de números enteros y devuelva una nueva matriz donde se hayan eliminado todas las filas que contienen al menos un número negativo. Además, la matriz resultante debe estar transpuesta (las filas se convierten en columnas y viceversa). Si la matriz resultante queda vacía, retorna una lista vacía.
# difficulty: Intermedio
# expected_output: [[1, 4], [2, 5], [3, 6]]
# hint: Primero filtra las filas que no tengan números negativos iterando sobre ellas. Luego, puedes usar la compresión de listas o la función zip con el operador de desempaquetado (*) para transponer la matriz resultante.

# === SOLUTION ===
def transponer_y_filtrar(matriz):
    if not matriz:
        return []
    
    # Filtrar filas que no contengan ningún número negativo
    filas_validas = [fila for fila in matriz if all(x >= 0 for x in fila)]
    
    if not filas_validas:
        return []
    
    # Transponer la matriz resultante
    matriz_transpuesta = [list(columna) for columna in zip(*filas_validas)]
    
    return matriz_transpuesta

# === TESTS ===
try:
    assert transponer_y_filtrar([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]], "Error: el test 1 ha fallado."
    assert transponer_y_filtrar([[1, -2, 3], [4, 5, 6]]) == [[4], [5], [6]], "Error: considera casos límites en tu lógica."
    assert transponer_y_filtrar([[-1, -2], [-3, -4]]) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")