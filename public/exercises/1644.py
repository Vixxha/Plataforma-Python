# === METADATA ===
# title: Búsqueda y Multiplicación de la Diagonal Principal
# description: Escribe una función que reciba una matriz cuadrada (representada como una lista de listas) y un número entero multiplicador. La función debe multiplicar cada elemento de la diagonal principal por dicho número y retornar la matriz modificada.
# difficulty: Intermedio
# expected_output: [[15, 2, 3], [4, 30, 6], [7, 8, 45]] para matriz = [[1, 2, 3], [4, 6, 6], [7, 8, 9]] y multiplicador = 5
# hint: Recuerda que los elementos de la diagonal principal de una matriz cuadrada son aquellos donde el índice de la fila es igual al índice de la columna (matriz[i][i]).

# === SOLUTION ===
def modificar_diagonal_principal(matriz, multiplicador):
    n = len(matriz)
    for i in range(n):
        matriz[i][i] *= multiplicador
    return matriz

# === TESTS ===
try:
    assert modificar_diagonal_principal([[1, 2], [3, 4]], 10) == [[10, 2], [3, 40]], "Error: el test 1 ha fallado."
    assert modificar_diagonal_principal([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 2) == [[2, 2, 3], [4, 10, 6], [7, 8, 18]], "Error: considera casos límites en tu lógica."
    assert modificar_diagonal_principal([[5]], 3) == [[15]], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")