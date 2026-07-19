# === METADATA ===
# title: Rotación de una Matriz Cuadrada
# description: Escribe una función que tome una matriz cuadrada (lista de listas) y la rote 90 grados en el sentido de las agujas del reloj. La rotación debe realizarse sobre la misma estructura o devolviendo una nueva.
# difficulty: Intermedio
# expected_output: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
# hint: Observa cómo cambia el índice (fila, columna) de cada elemento: el elemento en (i, j) termina en (j, n - 1 - i).

# === SOLUTION ===
def rotar_matriz(matriz):
    n = len(matriz)
    resultado = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            resultado[j][n - 1 - i] = matriz[i][j]
    return resultado

# === TESTS ===
try:
    assert rotar_matriz([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [[7, 4, 1], [8, 5, 2], [9, 6, 3]], "Error: el test 1 ha fallado."
    assert rotar_matriz([[1, 2], [3, 4]]) == [[3, 1], [4, 2]], "Error: considera casos límites en tu lógica."
    assert rotar_matriz([[5]]) == [[5]], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")