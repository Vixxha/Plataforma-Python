# === METADATA ===
# title: Transformación de Matriz en Vector de Máximos
# description: Dada una matriz (lista de listas) de números enteros, crea una función que devuelva una lista (vector) donde cada elemento sea el valor máximo de la fila correspondiente.
# difficulty: Intermedio
# expected_output: [10, 25, 9] para la entrada [[1, 10, 3], [25, 4, 8], [9, 0, 7]]
# hint: Puedes iterar sobre cada fila de la matriz y utilizar la función incorporada max() de Python para obtener el valor más alto de cada sublista.

# === SOLUTION ===
def obtener_maximos_por_fila(matriz):
    resultado = []
    for fila in matriz:
        resultado.append(max(fila))
    return resultado

# === TESTS ===
try:
    assert obtener_maximos_por_fila([[1, 10, 3], [25, 4, 8], [9, 0, 7]]) == [10, 25, 9], "Error: el test 1 ha fallado."
    assert obtener_maximos_por_fila([[5], [2], [8]]) == [5, 2, 8], "Error: considera casos límites en tu lógica."
    assert obtener_maximos_por_fila([[0, 0, 0], [-1, -5, -2]]) == [0, -1], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")