# === METADATA ===
# title: Analizador de Matriz Simétrica
# description: Escribe una función que reciba una matriz cuadrada (lista de listas) y determine si es simétrica, es decir, si la matriz es igual a su transpuesta (matriz[i][j] == matriz[j][i]).
# difficulty: Intermedio
# expected_output: True o False
# hint: Recuerda que para una matriz simétrica, el número de filas debe ser igual al número de columnas y debe cumplirse que matriz[i][j] == matriz[j][i] para todos los elementos.

# === SOLUTION ===
def es_simetrica(matriz):
    n = len(matriz)
    for i in range(n):
        if len(matriz[i]) != n:
            return False
        for j in range(i + 1, n):
            if matriz[i][j] != matriz[j][i]:
                return False
    return True

# === TESTS ===
try:
    assert es_simetrica([[1, 2, 3], [2, 4, 5], [3, 5, 6]]) == True, "Error: el test 1 ha fallado."
    assert es_simetrica([[1, 2], [3, 4]]) == False, "Error: considera casos límites en tu lógica."
    assert es_simetrica([[7]]) == True, "Error: el caso base (matriz 1x1) falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")