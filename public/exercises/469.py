# === METADATA ===
# title: Transformación de Matriz Escalonada
# description: Dada una lista de listas (matriz) de números enteros, escribe una función que multiplique todos los elementos de cada fila por el índice de dicha fila. Por ejemplo, la fila 0 se multiplica por 0, la fila 1 por 1, etc. Devuelve la nueva matriz resultante.
# difficulty: Intermedio
# expected_output: [[0, 0], [2, 4], [6, 9]] para input [[1, 2], [2, 4], [3, 4.5]]
# hint: Utiliza la función enumerate() para obtener tanto el índice de la fila como el contenido de la misma durante la iteración.

# === SOLUTION ===
def transformar_matriz(matriz):
    resultado = []
    for indice, fila in enumerate(matriz):
        nueva_fila = [elemento * indice for elemento in fila]
        resultado.append(nueva_fila)
    return resultado

# === TESTS ===
try:
    assert transformar_matriz([[1, 2], [2, 4], [3, 4]]) == [[0, 0], [2, 4], [6, 8]], "Error: el test 1 ha fallado."
    assert transformar_matriz([[5], [5], [5]]) == [[0], [5], [10]], "Error: considera casos límites en tu lógica."
    assert transformar_matriz([[]]) == [[]], "Error: el caso base (matriz vacía) falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")