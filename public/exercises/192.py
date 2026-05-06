# === METADATA ===
# title: Filtrado y Trasposición de Matriz
# description: Crea una función que reciba una matriz (lista de listas) de números enteros y devuelva una nueva matriz donde solo se incluyan las filas cuya suma sea par, y posteriormente, devuelva dicha matriz resultante transpuesta.
# difficulty: Intermedio
# expected_output: [[1, 3], [2, 4]] para una entrada [[1, 2], [3, 4]]
# hint: Primero filtra las filas usando una condición sobre la suma, luego utiliza zip(*matriz) para realizar la trasposición de forma eficiente.

# === SOLUTION ===
def filtrar_y_transponer(matriz):
    filas_filtradas = [fila for fila in matriz if sum(fila) % 2 == 0]
    if not filas_filtradas:
        return []
    return [list(columna) for columna in zip(*filas_filtradas)]

# === TESTS ===
try:
    assert filtrar_y_transponer([[1, 2], [3, 4]]) == [[1, 3], [2, 4]], "Error: el test 1 ha fallado."
    assert filtrar_y_transponer([[1, 1], [2, 2], [5, 5]]) == [[1, 2, 5], [1, 2, 5]], "Error: considera casos límites en tu lógica."
    assert filtrar_y_transponer([[1, 3], [5, 7]]) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")