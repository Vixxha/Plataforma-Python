# === METADATA ===
# title: Transponer y Filtrar Matriz
# description: Escribe una función que reciba una matriz (lista de listas) de números enteros y devuelva una nueva matriz donde se hayan eliminado todas las filas cuya suma total sea menor a un valor umbral dado. Además, la matriz resultante debe estar transpuesta (intercambiar filas por columnas).
# difficulty: Intermedio
# expected_output: [[1, 4], [2, 5], [3, 6]]
# hint: Primero calcula la suma de cada fila para filtrar cuáles se quedan. Luego, puedes usar comprensiones de listas anidadas o la función zip con el operador * para transponer la matriz resultante.

# === SOLUTION ===
def transponer_y_filtrar(matriz, umbral):
    if not matriz:
        return []
    
    # Filtrar filas cuya suma sea mayor o igual al umbral
    filas_filtradas = [fila for fila in matriz if sum(fila) >= umbral]
    
    if not filas_filtradas:
        return []
    
    # Transponer la matriz filtrada usando zip
    matriz_transpuesta = [list(columna) for columna in zip(*filas_filtradas)]
    
    return matriz_transpuesta

# === TESTS ===
try:
    assert transponer_y_filtrar([[1, 2, 3], [4, 5, 6], [1, 1, 1]], 10) == [[4], [5], [6]], "Error: el test 1 ha fallado."
    assert transponer_y_filtrar([[1, 2, 3], [4, 5, 6]], 5) == [[1, 4], [2, 5], [3, 6]], "Error: considera casos límites en tu lógica."
    assert transponer_y_filtrar([[1, 1], [1, 1]], 10) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")