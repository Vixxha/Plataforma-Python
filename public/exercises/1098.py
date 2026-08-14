# === METADATA ===
# title: Transponer y Filtrar Matriz
# description: Escribe una función que reciba una matriz (lista de listas) de números enteros y devuelva una nueva matriz transpuesta (intercambiando filas por columnas), pero omitiendo aquellos números que sean múltiplos de 3.
# difficulty: Intermedio
# expected_output: [[1, 4], [2, 5]]
# hint: Puedes recorrer la matriz original usando índices o la función zip(*matriz) para obtener las columnas, y luego aplicar una condición para filtrar los múltiplos de 3 (número % 3 != 0).

# === SOLUTION ===
def transponer_y_filtrar(matriz):
    if not matriz or not matriz[0]:
        return []
    
    # Transponemos la matriz usando zip
    transpuesta = [list(fila) for fila in zip(*matriz)]
    
    # Filtramos los múltiplos de 3
    resultado = [[num for num in fila if num % 3 != 0] for fila in transpuesta]
    
    return resultado

# === TESTS ===
try:
    assert transponer_y_filtrar([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5]], "Error: el test 1 ha fallado."
    assert transponer_y_filtrar([[3, 6], [9, 12]]) == [[], []], "Error: considera casos límites en tu lógica."
    assert transponer_y_filtrar([[1, 2], [3, 4], [5, 6]]) == [[1, 5], [2, 4]], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")