# === METADATA ===
# title: Analizador de Matriz Simétrica
# description: Escribe una función que reciba una matriz cuadrada (lista de listas) y determine si es simétrica. Una matriz es simétrica si es igual a su transpuesta (el elemento en la posición [i][j] es igual al elemento en [j][i]).
# difficulty: Intermedio
# expected_output: True o False
# hint: Debes comparar el elemento en la fila i y columna j con el elemento en la columna i y fila j para cada celda de la matriz.

# === SOLUTION ===
def es_matriz_simetrica(matriz):
    n = len(matriz)
    for i in range(n):
        for j in range(i + 1, n):
            if matriz[i][j] != matriz[j][i]:
                return False
    return True

# === TESTS ===
try:
    assert es_matriz_simetrica([[1, 2, 3], [2, 4, 5], [3, 5, 6]]) == True, "Error: el test 1 ha fallado."
    assert es_matriz_simetrica([[1, 2], [3, 4]]) == False, "Error: considera casos límites en tu lógica."
    assert es_matriz_simetrica([[5]]) == True, "Error: el caso base de matriz 1x1 falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")