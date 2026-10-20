# === METADATA ===
# title: Búsqueda y Reemplazo en Matriz
# description: Escribe una función que reciba una matriz (lista de listas) de números enteros, un valor objetivo y un valor de reemplazo. La función debe recorrer toda la matriz y reemplazar todas las apariciones del valor objetivo por el valor de reemplazo, devolviendo la matriz modificada.
# difficulty: Intermedio
# expected_output: [[1, 9, 3], [9, 5, 9], [7, 8, 9]] para la matriz [[1, 2, 3], [2, 5, 2], [7, 8, 2]], buscando el 2 y reemplazando por 9.
# hint: Puedes utilizar bucles anidados para recorrer cada elemento especificando su fila y columna, o recorrer las filas y usar el método de reemplazo en listas.

# === SOLUTION ===
def reemplazar_en_matriz(matriz, objetivo, reemplazo):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == objetivo:
                matriz[i][j] = reemplazo
    return matriz

# === TESTS ===
try:
    assert reemplazar_en_matriz([[1, 2, 3], [2, 5, 2], [7, 8, 2]], 2, 9) == [[1, 9, 3], [9, 5, 9], [7, 8, 9]], "Error: el test 1 ha fallado."
    assert reemplazar_en_matriz([[0, 0], [0, 0]], 0, 1) == [[1, 1], [1, 1]], "Error: considera casos límites en tu lógica."
    assert reemplazar_en_matriz([[5, 6], [7, 8]], 9, 1) == [[5, 6], [7, 8]], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")