# === METADATA ===
# title: Filtrar y Trasponer Matriz Diagonal
# description: Escribe una función que reciba una matriz cuadrada (lista de listas) de números enteros. La función debe retornar una nueva matriz donde todos los elementos que se encuentren por encima de la diagonal principal sean reemplazados por 0, y luego devolver la matriz resultante.
# difficulty: Intermedio
# expected_output: [[1, 0, 0], [4, 5, 0], [7, 8, 9]]
# hint: Usa bucles anidados utilizando los índices `i` y `j`. Si la columna `j` es mayor que la fila `i`, el valor debe ser 0.

# === SOLUTION ===
def procesar_matriz_diagonal(matriz):
    n = len(matriz)
    resultado = [fila[:] for fila in matriz]
    for i in range(n):
        for j in range(n):
            if j > i:
                resultado[i][j] = 0
    return resultado

# === TESTS ===
try:
    assert procesar_matriz_diagonal([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [[1, 0, 0], [4, 5, 0], [7, 8, 9]], "Error: el test 1 ha fallado."
    assert procesar_matriz_diagonal([[5, 1], [2, 3]]) == [[5, 0], [2, 3]], "Error: considera casos límites en tu lógica."
    assert procesar_matriz_diagonal([[10]]) == [[10]], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")