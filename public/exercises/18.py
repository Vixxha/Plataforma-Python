# === METADATA ===
# title: Filtrado y Trasposición de Matriz
# description: Crea una función que reciba una matriz (lista de listas) y devuelva una nueva matriz donde solo se mantengan las filas cuya suma de elementos sea mayor a 10. Posteriormente, devuelve la matriz resultante transpuesta (filas se convierten en columnas).
# difficulty: Intermedio
# expected_output: [[1, 4], [2, 5], [3, 6]]
# hint: Primero filtra las filas usando una lista por comprensión y luego usa zip(*matriz) para transponer.

# === SOLUTION ===
def procesar_matriz(matriz):
    filas_filtradas = [fila for fila in matriz if sum(fila) > 10]
    if not filas_filtradas:
        return []
    return [list(columna) for columna in zip(*filas_filtradas)]

# === TESTS ===
try:
    assert procesar_matriz([[1, 2, 3], [4, 5, 6], [1, 1, 1]]) == [[1, 4], [2, 5], [3, 6]], "Error: el test 1 ha fallado."
    assert procesar_matriz([[1, 1], [2, 2]]) == [], "Error: considera casos donde ninguna fila suma más de 10."
    assert procesar_matriz([[10, 10], [5, 6]]) == [[10, 5], [10, 6]], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")