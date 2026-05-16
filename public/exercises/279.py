# === METADATA ===
# title: Transformación de Matriz en Vector de Máximos
# description: Dada una matriz (lista de listas) de números enteros, crea una función que retorne una nueva lista (vector) donde cada elemento sea el valor máximo encontrado en cada fila de la matriz original.
# difficulty: Intermedio
# expected_output: [5, 9, 8]
# hint: Puedes iterar sobre cada sub-lista y utilizar la función incorporada 'max()' de Python para obtener el mayor valor de cada fila.

# === SOLUTION ===
def obtener_maximos_por_fila(matriz):
    resultado = []
    for fila in matriz:
        if len(fila) > 0:
            resultado.append(max(fila))
        else:
            resultado.append(None)
    return resultado

# === TESTS ===
try:
    assert obtener_maximos_por_fila([[1, 2, 5], [9, 3, 4], [8, 6, 7]]) == [5, 9, 8], "Error: el test 1 ha fallado."
    assert obtener_maximos_por_fila([[10, -2], [0, 0], [5, 10, 2]]) == [10, 0, 10], "Error: considera casos límites en tu lógica."
    assert obtener_maximos_por_fila([[], [1]]) == [None, 1], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")