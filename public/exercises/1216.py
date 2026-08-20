# === METADATA ===
# title: Operaciones con Matrices: Suma de la Diagonal Principal
# description: Escribe una función que reciba una matriz cuadrada (representada como una lista de listas de números) y calcule la suma de los elementos que pertenecen a su diagonal principal (donde el índice de la fila es igual al índice de la columna).
# difficulty: Intermedio
# expected_output: 15
# hint: Puedes recorrer la matriz usando un solo ciclo `for` con el rango del tamaño de la matriz, sumando los elementos donde el índice de la fila y la columna son iguales `matriz[i][i]`.

# === SOLUTION ===
def suma_diagonal_principal(matriz):
    if not matriz or not matriz[0]:
        return 0
    
    suma = 0
    for i in range(len(matriz)):
        suma += matriz[i][i]
    return suma

# === TESTS ===
try:
    assert suma_diagonal_principal([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 15, "Error: el test 1 ha fallado."
    assert suma_diagonal_principal([[5]]) == 5, "Error: considera casos límites en tu lógica."
    assert suma_diagonal_principal([[1, 0], [0, 1]]) == 2, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")