# === METADATA ===
# title: Filtrado y Trasposición de Matriz
# description: Crea una función que reciba una matriz (lista de listas) y devuelva una nueva matriz donde solo se mantengan las filas cuya suma de elementos sea mayor a 10. Posteriormente, devuelve la matriz resultante transpuesta (filas convertidas en columnas).
# difficulty: Intermedio
# expected_output: [[1, 5], [2, 6], [8, 0]] para input [[1, 2, 8], [5, 6, 0], [1, 1, 1]]
# hint: Primero filtra las filas usando una comprensión de lista o un bucle, luego usa zip(*matriz) para transponer.

# === SOLUTION ===
def filtrar_y_transponer(matriz):
    # Filtrar filas cuya suma sea mayor a 10
    filtradas = [fila for fila in matriz if sum(fila) > 10]
    
    # Transponer usando zip y convertir tuplas a listas
    if not filtradas:
        return []
    return [list(columna) for columna in zip(*filtradas)]

# === TESTS ===
try:
    assert filtrar_y_transponer([[10, 1], [1, 1], [5, 6]]) == [[10, 5], [1, 6]], "Error: el test 1 ha fallado."
    assert filtrar_y_transponer([[1, 1], [2, 2]]) == [], "Error: considera casos donde ninguna fila cumple la condición."
    assert filtrar_y_transponer([[5, 6, 2], [10, 2, 1]]) == [[5, 10], [6, 2], [2, 1]], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")