# === METADATA ===
# title: Filtro de Matrices Cuadradas
# description: Crea una función que reciba una matriz cuadrada (lista de listas) y devuelva una lista simple con todos aquellos elementos que se encuentren en la diagonal principal (donde el índice de fila es igual al índice de columna).
# difficulty: Intermedio
# expected_output: [1, 5, 9] para una matriz de 3x3 con números del 1 al 9.
# hint: Utiliza un bucle for o comprensión de listas recorriendo los índices desde 0 hasta el largo de la matriz.

# === SOLUTION ===
def extraer_diagonal(matriz):
    resultado = []
    for i in range(len(matriz)):
        resultado.append(matriz[i][i])
    return resultado

# === TESTS ===
try:
    assert extraer_diagonal([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 5, 9], "Error: el test 1 ha fallado."
    assert extraer_diagonal([[10, 2], [3, 4]]) == [10, 4], "Error: considera casos límites en tu lógica."
    assert extraer_diagonal([[5]]) == [5], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")