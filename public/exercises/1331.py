# === METADATA ===
# title: Transponer y Promediar una Matriz
# description: Escribe una función que reciba una matriz (lista de listas) de números enteros o flotantes, calcule su transpuesta (intercambiar filas por columnas) y devuelva una nueva matriz donde cada elemento sea el resultado de truncar a 2 decimales, o simplemente calcula el promedio de cada columna devolviendo una lista con dichos promedios. Mejor hagamos algo más directo: Escribe una función que reciba una matriz cuadrada y devuelva la suma de los elementos que se encuentran en su diagonal principal.
# difficulty: Básico-Intermedio
# expected_output: 15
# hint: Puedes recorrer la matriz usando un solo ciclo `for` aprovechando que en una matriz cuadrada el índice de la fila y el de la columna son iguales para la diagonal principal (es decir, el elemento en la posición `[i][i]`).

# === SOLUTION ===
def suma_diagonal_principal(matriz):
    suma = 0
    for i in range(len(matriz)):
        suma += matriz[i][i]
    return suma

# === TESTS ===
try:
    assert suma_diagonal_principal([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 15, "Error: el test 1 ha fallado."
    assert suma_diagonal_principal([[10, 2], [3, 4]]) == 14, "Error: considera casos límites en tu lógica."
    assert suma_diagonal_principal([[5]]) == 5, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")