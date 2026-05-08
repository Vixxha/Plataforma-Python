# === METADATA ===
# title: Filtro de Matrices Cuadradas
# description: Crea una función que reciba una matriz cuadrada (lista de listas) y devuelva una lista unidimensional con todos los elementos de la diagonal principal multiplicados por 2.
# difficulty: Intermedio
# expected_output: [2, 10, 18] para una matriz de entrada [[1, 2], [3, 5], [4, 6, 9]] donde la diagonal es [1, 5, 9]
# hint: Recuerda que en una matriz cuadrada, los elementos de la diagonal principal son aquellos donde el índice de fila es igual al índice de columna (i == j).

# === SOLUTION ===
def procesar_diagonal(matriz):
    resultado = []
    for i in range(len(matriz)):
        resultado.append(matriz[i][i] * 2)
    return resultado

# === TESTS ===
try:
    assert procesar_diagonal([[1, 2], [3, 5]]) == [2, 10], "Error: el test 1 ha fallado."
    assert procesar_diagonal([[1, 0, 0], [0, 5, 0], [0, 0, 9]]) == [2, 10, 18], "Error: considera casos límites en tu lógica."
    assert procesar_diagonal([[10]]) == [20], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")