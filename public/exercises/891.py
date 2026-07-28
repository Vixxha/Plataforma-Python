# === METADATA ===
# title: Filtrar y Multiplicar la Diagonal Principal
# description: Escribe una función que reciba una matriz cuadrada (lista de listas de números) y devuelva una lista con los elementos de la diagonal principal multiplicados por 2, pero filtrando y conservando únicamente aquellos valores que sean números pares.
# difficulty: Intermedio
# expected_output: [4, 12]
# hint: La diagonal principal de una matriz cuadrada está formada por los elementos donde el índice de la fila es igual al índice de la columna (matriz[i][i]).

# === SOLUTION ===
def procesar_diagonal_principal(matriz):
    resultado = []
    for i in range(len(matriz)):
        valor = matriz[i][i] * 2
        if valor % 2 == 0:
            resultado.append(valor)
    return resultado

# === TESTS ===
try:
    assert procesar_diagonal_principal([[1, 2], [3, 4]]) == [4], "Error: el test 1 ha fallado."
    assert procesar_diagonal_principal([[2, 0, 1], [0, 3, 5], [1, 5, 6]]) == [4, 6, 12], "Error: considera casos límites en tu lógica."
    assert procesar_diagonal_principal([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [10], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")