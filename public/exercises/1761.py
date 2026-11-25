# === METADATA ===
# title: Filtrar y Trasponer Matriz Diagonal
# description: Escribe una función que reciba una matriz cuadrada (lista de listas) de números enteros. La función debe extraer todos los elementos de la diagonal principal, filtrar aquellos que sean números pares, y devolver una nueva lista con los pares encontrados multiplicados por 2.
# difficulty: Intermedio
# expected_output: [4, 12]
# hint: La diagonal principal de una matriz cuadrada está formada por los elementos donde el índice de la fila es igual al índice de la columna (matriz[i][i]).

# === SOLUTION ===
def procesar_diagonal_par(matriz):
    resultado = []
    for i in range(len(matriz)):
        elemento = matriz[i][i]
        if elemento % 2 == 0:
            resultado.append(elemento * 2)
    return resultado

# === TESTS ===
try:
    assert procesar_diagonal_par([[2, 1, 3], [4, 5, 6], [7, 8, 9]]) == [4, 10], "Error: el test 1 ha fallado."
    assert procesar_diagonal_par([[1, 2], [3, 4]]) == [8], "Error: considera casos límites en tu lógica."
    assert procesar_diagonal_par([[3, 1], [1, 5]]) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")