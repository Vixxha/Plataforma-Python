# === METADATA ===
# title: Filtrar y Trasponer Matriz
# description: Escribe una función que reciba una matriz cuadrada (lista de listas) de números enteros y devuelva una nueva matriz donde cada elemento original haya sido multiplicado por 2, pero solo si dicho elemento es un número par. Si es impar, el valor debe ser reemplazado por 0. Además, la matriz resultante debe estar transpuesta (intercambiar filas por columnas).
# difficulty: Intermedio
# expected_output: [[2, 0], [0, 8]] para la entrada [[1, 2], [0, 4]]
# hint: Puedes recorrer la matriz usando bucles anidados o listas por comprensión para aplicar la condición, y luego utilizar la indexación inversa o zip para realizar la transposición.

# === SOLUTION ===
def filtrar_y_trasponer(matriz):
    n = len(matriz)
    procesada = [[(val * 2 if val % 2 == 0 else 0) for val in fila] for fila in matriz]
    traspuesta = [[procesada[j][i] for j in range(n)] for i in range(n)]
    return traspuesta

# === TESTS ===
try:
    assert filtrar_y_trasponer([[1, 2], [3, 4]]) == [[0, 0], [4, 8]], "Error: el test 1 ha fallado."
    assert filtrar_y_trasponer([[2, 4], [6, 8]]) == [[4, 12], [8, 16]], "Error: considera casos límites en tu lógica."
    assert filtrar_y_trasponer([[1, 1, 1], [2, 2, 2], [3, 3, 3]]) == [[0, 4, 0], [0, 4, 0], [0, 4, 0]], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")