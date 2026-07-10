# === METADATA ===
# title: Filtrado y Trasposición de Matriz
# description: Crea una función que reciba una matriz (lista de listas) y devuelva una nueva matriz donde solo se incluyan las filas cuya suma de elementos sea mayor a 10. Posteriormente, devuelve la matriz transpuesta resultante.
# difficulty: Intermedio
# expected_output: [[1, 4], [8, 5], [3, 2]] para la entrada [[1, 8, 3], [4, 5, 2]]
# hint: Primero filtra las filas usando una lista por comprensión o un bucle. Para transponer, puedes usar zip(*matriz) o dos bucles anidados.

# === SOLUTION ===
def procesar_matriz(matriz):
    filas_filtradas = [fila for fila in matriz if sum(fila) > 10]
    if not filas_filtradas:
        return []
    return [list(columna) for columna in zip(*filas_filtradas)]

# === TESTS ===
try:
    assert procesar_matriz([[1, 8, 3], [4, 5, 2]]) == [[1, 4], [8, 5], [3, 2]], "Error: el test 1 ha fallado."
    assert procesar_matriz([[1, 1], [2, 2]]) == [], "Error: debería devolver lista vacía si ninguna fila suma > 10."
    assert procesar_matriz([[10, 1], [5, 6]]) == [[10, 5], [1, 6]], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")