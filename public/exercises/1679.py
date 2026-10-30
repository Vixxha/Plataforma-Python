# === METADATA ===
# title: Filtrar y Trasponer Matriz
# description: Escribe una función que reciba una matriz (lista de listas) de números enteros. La función debe retornar una nueva matriz donde se eliminen todas las filas que contengan al menos un número negativo, y posteriormente aplicar una trasposición (intercambiar filas por columnas) a la matriz resultante. Si la matriz queda vacía tras el filtrado, debe retornar una lista vacía.
# difficulty: Intermedio
# expected_output: [[2, 5], [4, 6]] para la entrada [[1, -2, 3], [2, 4, 5], [5, 6, 7]]
# hint: Primero filtra las filas que no tengan números negativos creando una nueva lista de listas. Luego, asegúrate de manejar el caso donde la matriz filtrada esté vacía antes de intentar la trasposición usando la función zip(*matriz).

# === SOLUTION ===
def filtrar_y_trasponer(matriz):
    if not matriz or not matriz[0]:
        return []
    
    # Filtrar filas que no contengan ningún número negativo
    filas_validas = [fila for fila in matriz if all(x >= 0 for x in fila)]
    
    if not filas_validas:
        return []
    
    # Trasponer la matriz resultante
    matriz_transpuesta = [list(columna) for columna in zip(*filas_validas)]
    
    return matriz_transpuesta

# === TESTS ===
try:
    assert filtrar_y_trasponer([[1, -2, 3], [2, 4, 5], [5, 6, 7]]) == [[2, 5], [4, 6], [5, 7]], "Error: el test 1 ha fallado."
    assert filtrar_y_trasponer([[-1, -2], [-3, -4]]) == [], "Error: considera casos límites en tu lógica."
    assert filtrar_y_trasponer([[1, 2], [3, 4]]) == [[1, 3], [2, 4]], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")