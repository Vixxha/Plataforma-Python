# === METADATA ===
# title: Filtrar y Trasponer Matriz
# description: Escribe una función que reciba una matriz (lista de listas) de números enteros y devuelva una nueva matriz donde se hayan eliminado todas las filas que contengan al menos un número negativo. Luego, la matriz resultante debe ser traspuesta (intercambiar filas por columnas). Si la matriz resultante queda vacía, debe retornar una lista vacía.
# difficulty: Intermedio
# expected_output: [[1, 4], [2, 5], [3, 6]]
# hint: Primero filtra las filas que no tengan negativos iterando sobre ellas. Luego, puedes usar comprensión de listas con `zip` para transponer la matriz resultante.

# === SOLUTION ===
def filtrar_y_trasponer(matriz):
    if not matriz:
        return []
    
    # Filtrar filas que no contengan ningún número negativo
    filas_validas = [fila for fila in matriz if all(x >= 0 for x in fila)]
    
    if not filas_validas:
        return []
    
    # Trasponer la matriz utilizando zip
    matriz_traspuesta = [list(columna) for columna in zip(*filas_validas)]
    
    return matriz_traspuesta

# === TESTS ===
try:
    assert filtrar_y_trasponer([[1, 2, 3], [4, 5, 6], [-1, 2, 3]]) == [[1, 4], [2, 5], [3, 6]], "Error: el test 1 ha fallado."
    assert filtrar_y_trasponer([[-1, -2], [3, 4], [5, -6]]) == [[3, 5], [4]], "Error: considera casos límites en tu lógica."
    assert filtrar_y_trasponer([[-1, -2], [-3, -4]]) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")