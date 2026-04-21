# === METADATA ===
# title: Filtrado de Matriz Simétrica
# description: Dada una matriz cuadrada (lista de listas) de números enteros, escribe una función que devuelva una nueva lista conteniendo únicamente los elementos que se encuentran en la diagonal principal (donde el índice de fila es igual al índice de columna) y que además sean números pares.
# difficulty: Intermedio
# expected_output: [2, 8] para una matriz donde la diagonal tiene valores [2, 3, 8]
# hint: Recorre la matriz usando un solo bucle for basado en el tamaño de la matriz (longitud de la lista exterior) para acceder a los índices [i][i].

# === SOLUTION ===
def filtrar_diagonal_pares(matriz):
    resultado = []
    n = len(matriz)
    for i in range(n):
        valor = matriz[i][i]
        if valor % 2 == 0:
            resultado.append(valor)
    return resultado

# === TESTS ===
try:
    assert filtrar_diagonal_pares([[2, 1, 3], [4, 3, 5], [6, 7, 8]]) == [2, 8], "Error: el test 1 ha fallado."
    assert filtrar_diagonal_pares([[1, 0], [0, 5]]) == [0], "Error: considera casos límites en tu lógica."
    assert filtrar_diagonal_pares([[7, 0, 0], [0, 9, 0], [0, 0, 11]]) == [], "Error: el caso base falló (ningún par)."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")