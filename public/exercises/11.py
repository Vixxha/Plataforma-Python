# === METADATA ===
# title: Filtrado y Suma de Diagonales
# description: Crea una función que reciba una matriz cuadrada (lista de listas) y devuelva la suma de los elementos que se encuentran en su diagonal principal (índices donde fila == columna).
# difficulty: Intermedio
# expected_output: 15
# hint: Utiliza un único bucle for que recorra el índice i desde 0 hasta el tamaño de la matriz, accediendo a matriz[i][i].

# === SOLUTION ===
def sumar_diagonal(matriz):
    suma = 0
    for i in range(len(matriz)):
        suma += matriz[i][i]
    return suma

# === TESTS ===
try:
    assert sumar_diagonal([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 15, "Error: el test 1 ha fallado."
    assert sumar_diagonal([[10, 0], [0, 5]]) == 15, "Error: considera casos límites en tu lógica."
    assert sumar_diagonal([[7]]) == 7, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")