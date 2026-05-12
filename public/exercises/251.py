# === METADATA ===
# title: Transformación de Matriz Escalonada
# description: Dada una matriz de números (lista de listas), escribe una función que devuelva una nueva lista con la suma de cada fila, pero multiplicada por el índice de esa fila (empezando en 0).
# difficulty: Intermedio
# expected_output: Para [[1, 2], [3, 4]], el resultado debería ser [0, 14]
# hint: Utiliza la función enumerate() para obtener tanto el índice como la fila durante la iteración.

# === SOLUTION ===
def transformar_matriz(matriz):
    resultado = []
    for i, fila in enumerate(matriz):
        suma_fila = sum(fila)
        resultado.append(suma_fila * i)
    return resultado

# === TESTS ===
try:
    assert transformar_matriz([[1, 2], [3, 4]]) == [0, 14], "Error: el test 1 ha fallado."
    assert transformar_matriz([[10], [5], [2]]) == [0, 5, 4], "Error: considera casos límites en tu lógica."
    assert transformar_matriz([]) == [], "Error: el caso base (matriz vacía) falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")