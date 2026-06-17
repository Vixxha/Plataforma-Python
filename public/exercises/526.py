# === METADATA ===
# title: Filtrado y Trasposición de Matriz
# description: Escribe una función que reciba una matriz (lista de listas) de números enteros y devuelva una nueva matriz donde solo se incluyan las filas cuya suma de elementos sea mayor o igual a 10. Posteriormente, devuelve la matriz resultante transpuesta (las filas pasan a ser columnas).
# difficulty: Intermedio
# expected_output: [[1, 7], [8, 2], [9, 3]]
# hint: Primero filtra las listas internas usando una comprensión de lista o un bucle, y luego usa `zip(*matriz)` para transponer el resultado.

# === SOLUTION ===
def filtrar_y_transponer(matriz):
    filas_filtradas = [fila for fila in matriz if sum(fila) >= 10]
    if not filas_filtradas:
        return []
    return [list(columna) for columna in zip(*filas_filtradas)]

# === TESTS ===
try:
    assert filtrar_y_transponer([[1, 2], [5, 5], [7, 2]]) == [[5, 7], [5, 2]], "Error: el test 1 ha fallado."
    assert filtrar_y_transponer([[1, 1], [2, 2]]) == [], "Error: considera casos donde ninguna fila cumple la condición."
    assert filtrar_y_transponer([[10, 0], [0, 10]]) == [[10, 0], [0, 10]], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")