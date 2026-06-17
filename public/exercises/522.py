# === METADATA ===
# title: Filtrado y Trasposición de Matriz
# description: Crea una función que reciba una matriz (lista de listas) de números enteros y devuelva una nueva matriz donde solo se conserven los números pares, sustituyendo los impares por 0, y finalmente devuelva la matriz transpuesta (intercambiando filas por columnas).
# difficulty: Intermedio
# expected_output: [[2, 0], [0, 4]] para la entrada [[2, 0], [1, 4]]
# hint: Primero recorre la matriz para aplicar el filtro de paridad y luego usa una comprensión de listas con zip(*matriz) para realizar la transposición.

# === SOLUTION ===
def filtrar_y_transponer(matriz):
    # Filtrar pares
    filtrada = [[num if num % 2 == 0 else 0 for num in fila] for fila in matriz]
    # Transponer usando zip
    return [list(fila) for fila in zip(*filtrada)]

# === TESTS ===
try:
    assert filtrar_y_transponer([[1, 2], [3, 4]]) == [[0, 0], [2, 4]], "Error: el test 1 ha fallado."
    assert filtrar_y_transponer([[5, 7], [9, 11]]) == [[0, 0], [0, 0]], "Error: considera casos límites en tu lógica."
    assert filtrar_y_transponer([[2, 4, 6]]) == [[2], [4], [6]], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")