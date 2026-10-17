# === METADATA ===
# title: Matriz de Calor Diaria
# description: Escribe una función que reciba una matriz (lista de listas) de números enteros que representan las temperaturas registradas en diferentes ciudades (filas) durante varios días (columnas). La función debe devolver una nueva lista que contenga la temperatura máxima registrada en cada ciudad.
# difficulty: Intermedio
# expected_output: [15, 22, 19]
# hint: Puedes recorrer cada fila de la matriz y utilizar la función incorporada max() de Python para encontrar el valor más alto de esa fila.

# === SOLUTION ===
def temperatura_maxima_por_ciudad(matriz):
    return [max(fila) for fila in matriz]

# === TESTS ===
try:
    assert temperatura_maxima_por_ciudad([[5, 12, 8], [15, 22, 19], [10, 14, 18]]) == [12, 22, 18], "Error: el test 1 ha fallado."
    assert temperatura_maxima_por_ciudad([[1, 2, 3], [4, 5, 6]]) == [3, 6], "Error: considera casos límites en tu lógica."
    assert temperatura_maxima_por_ciudad([[-5, -2, -10], [0, 5, 3]]) == [-2, 5], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")